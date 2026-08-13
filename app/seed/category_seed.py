from app import app, db
from app.framework.seed import Seedable
from app.models.category import Category


class CategorySeed(Seedable):
    """Les catégories de l'application.

    order = 10: ce seeder passe avant tous les autres (order par défaut = 100),
    parce que ticketSeed a besoin des catégories pour les attribuer.
    """

    order = 10

    # (category_name, category_description)
    CATEGORIES = [
        ("Hardware", "problème composant physique "),
        ("Software", "Problème logiciel"),
    ]

    def seed(self):
        for category_name, category_description in self.CATEGORIES:
            if Category.query.filter_by(category_name=category_name).first() is not None:
                app.logger.debug(f"Seed category {category_name}: déjà présent")
                continue

            category = Category(category_name=category_name,
                                 category_description=category_description)
            db.session.add(category)

            app.logger.debug(f"Seed Category {category_name}")

        # Un seul commit pour tous les CATEGORIES: soit tout passe, soit rien
        # (une transaction). Le try/except est dans Seed.__seed, qui logue
        # l'erreur et continue avec les seeders suivants.
        db.session.commit()