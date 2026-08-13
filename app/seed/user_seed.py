from argon2 import PasswordHasher

from app import app, db
from app.framework.seed import Seedable
from app.models import Role, RoleStatus, User


class UserSeed(Seedable):
    """Les comptes de démonstration.

    order = 20: après RoleSeed (10), parce qu'on attribue des rôles ici.
    """

    order = 20

    # (username, mot de passe en clair, email, user_firstname, user_lastname, rôles)
    USERS = [
        ("admin", "admin", "admin@example.com", "Roboute", "Guilliman",
         [RoleStatus.CLIENT, RoleStatus.ADMIN]),
        ("test", "test", "test@example.com", "Toto", "tutu",
         [RoleStatus.CLIENT]),
    ]

    def seed(self):
        hasher = PasswordHasher()

        for username, password, email, user_firstname, user_lastname, role_names in self.USERS:
            if User.query.filter_by(username=username).first() is not None:
                app.logger.debug(f"Seed user {username}: déjà présent")
                continue

            user = User(username=username,
                        user_email=email,
                        # Jamais de mot de passe en clair en base, même pour un
                        # jeu de données de test: on prend les mêmes habitudes
                        # partout.
                        user_password=hasher.hash(password),
                        user_firstname=user_firstname,
                        user_lastname=user_lastname)

            # add() AVANT d'attribuer les rôles: sans ça, la requête
            # Role.query.filter_by(...) de la boucle déclenche un autoflush
            # alors que les UserRole créés ne sont rattachés à aucune session
            # (SQLAlchemy émet un SAWarning et n'insère pas la liaison).
            db.session.add(user)

            for role_name in role_names:
                role = Role.query.filter_by(role_name=role_name).first()

                if role is None:
                    # Ne devrait pas arriver grâce à `order`, mais un seeder ne
                    # doit pas partir du principe que la base est parfaite.
                    app.logger.warning(f"Seed user {username}: rôle {role_name} absent")
                    continue

                user.add_role(role)

            app.logger.debug(f"Seed user {username}")

        # Un seul commit pour tous les users: soit tout passe, soit rien
        # (une transaction). Le try/except est dans Seed.__seed, qui logue
        # l'erreur et continue avec les seeders suivants.
        db.session.commit()
