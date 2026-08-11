from app import db
from app.models.base_entity import BaseEntity
from app.models.role import Role
from app.models.user_role import UserRole


class User(BaseEntity, db.Model):
    """Un utilisateur du site.

    Le mot de passe n'est JAMAIS stocké en clair: la colonne contient un hash
    argon2 (voir UserService.insert). On ne peut pas "décoder" un hash, on peut
    seulement revérifier un mot de passe candidat.
    """

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    user_email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    # 255 caractères: un hash argon2 fait ~100 caractères, on prévoit large.
    user_password = db.Column(db.String(255), nullable=False)

    user_firstname = db.Column(db.String(127), nullable=False)
    user_lastname = db.Column(db.String(127), nullable=False)

    team_id = db.Column(db.ForeignKey('teams.team_id'), nullable=True)
    site_id = db.Column(db.ForeignKey('sites.site_id'), nullable=True)



    # cascade='all, delete-orphan': supprimer un user supprime ses lignes
    # d'association (sinon la base refuserait, à cause des clés étrangères).
    roles = db.relationship('UserRole', back_populates='user', cascade='all, delete-orphan')
    team = db.relationship('Team', back_populates='members')
    site = db.relationship('Site', back_populates='users')

    tickets_created = db.relationship('Ticket',foreign_keys='Ticket.author_id', back_populates='author')
    tickets_assigned = db.relationship('Ticket',foreign_keys='Ticket.technician_id', back_populates='technician')

    comments = db.relationship('Comment', back_populates='author')
    ticket_status_histories = db.relationship('TicketStatusHistory', back_populates='user')
    equipments = db.relationship('Equipment', back_populates='user')
    knowledge_articles = db.relationship('KnowledgeArticle', back_populates='author')
    satisfaction_surveys = db.relationship('SatisfactionSurvey', back_populates='client')
    interventions = db.relationship('Intervention', back_populates='technician')

    # --- logique métier -----------------------------------------------------
    # Un modèle n'est pas qu'un sac de colonnes: les règles qui ne concernent
    # que l'entité elle-même vivent ici, pas dans le service ni le controller.

    def add_role(self, role: Role):
        """Ajoute un rôle (sans doublon)."""
        if role.role_name in self.role_names():
            return

        user_role = UserRole()
        user_role.role = role
        user_role.user = self
        self.roles.append(user_role)

    def get_roles(self):
        """ """
        return self.roles



    def remove_role(self, role: Role):
        """Retire un rôle s'il est présent."""
        for user_role in self.roles: # TODO : Check Warning ?
            if user_role.role.role_name == role.role_name:
                self.roles.remove(user_role)
                break

    def role_names(self) -> list[str]:
        return [user_role.role.role_name for user_role in self.roles]

    def has_role(self, role: str) -> bool:
        return role in self.role_names()

    def is_admin(self) -> bool:
        return self.has_role("ADMIN")

    def __repr__(self):
        return f"<User {self.user_name}>"
