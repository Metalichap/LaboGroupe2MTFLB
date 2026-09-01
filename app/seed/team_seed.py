from app import app, db
from app.framework.seed import Seedable
from app.models.team import Team


class TeamSeed(Seedable):
    """Les catégories de l'application.

    order = 10: ce seeder passe avant tous les autres (order par défaut = 100),
    parce que ticketSeed a besoin des catégories pour les attribuer.
    """

    order = 10

    # (category_name, category_description)
    TEAMS = [
        ("Peak", "J'ai glissé chef !"),
        ("Café", "Toujours en pause."),
    ]

    def seed(self):
        for team_name, team_description in self.TEAMS:
            if Team.query.filter_by(team_name=team_name).first() is not None:
                app.logger.debug(f"Seed Team {team_name}: déjà présent")
                continue

            team = Team(
                team_name=team_name,
                team_description=team_description
            )

            db.session.add(team)

            app.logger.debug(f"Seed Team {team_name}")

        # Un seul commit pour tous les CATEGORIES: soit tout passe, soit rien
        # (une transaction). Le try/except est dans Seed.__seed, qui logue
        # l'erreur et continue avec les seeders suivants.
        db.session.commit()