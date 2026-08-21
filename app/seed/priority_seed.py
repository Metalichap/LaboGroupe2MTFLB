from app import app, db
from app.framework.seed import Seedable
from app.models.priority import Priority, PriorityLevel


class PrioritySeed(Seedable):
    """Les priority pour les ticket
    """

    order = 10  #needed pour les tickets

    # (priority_name, priority_level, priority_delay_hours)
    PRIORITIES = [
        ("Urgent", PriorityLevel.URGENT, 4),
        ("Normal", PriorityLevel.NORMAL, 24),
        ("Faible", PriorityLevel.LOW, 72),
    ]

    def seed(self):
        for priority_name, priority_level, priority_delay_hours in self.PRIORITIES:
            if Priority.query.filter_by(priority_name=priority_name).first() is not None:
                app.logger.debug(f"Seed priority {priority_name}: déjà présent")
                continue

            priority = Priority(priority_name=priority_name,
                                 priority_level=priority_level,
                                 priority_delay_hours=priority_delay_hours)
            db.session.add(priority)

            app.logger.debug(f"Seed Priority {priority_name}")

        # Un seul commit pour toutes les PRIORITIES: soit tout passe, soit rien
        # (une transaction). Le try/except est dans Seed.__seed, qui logue
        # l'erreur et continue avec les seeders suivants.
        db.session.commit()