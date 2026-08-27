from datetime import datetime, timedelta, timezone

from app import app, db
from app.dtos.ticket_dto import TicketDTO
from app.forms.ticket.ticket_create_form import TicketCreateForm
from app.forms.ticket.ticket_update_form import TicketUpdateForm
from app.framework.decorators.injectable import injectable
from app.mappers.ticket_mapper import TicketMapper
from app.models.ticket import Ticket
from app.models.priority import Priority
from app.services.base_service import BaseService
from app.dtos.user_dto import UserDTO


@injectable
class TicketService(BaseService):
    """Ticket CRUD"""

    # --- Crud -----------------------------------------------------------
    
    def insert(self, form: TicketCreateForm, author_id: int) -> TicketDTO | None:
        """Création d'un nouveau ticket.
        """

        #récupération de la priorité pour le calcul du SLA et de la due_date. Si la priorité envoyé est introuvable, on interomp le process
        priority = Priority.query.filter_by(priority_id=form.priority_id.data).first()
        if priority is None:
            app.logger.error(f"insert ticket: priority {form.priority_id.data} introuvable")
            return None
        ticket = Ticket()
        TicketMapper.form_to_entity(form, ticket)
        ticket.author_id = author_id
        ticket.ticket_due_date = datetime.now(timezone.utc) + timedelta(hours=priority.priority_delay_hours)

        try:
            db.session.add(ticket)
            db.session.commit()
        except Exception as e:
            app.logger.error(f"insert ticket: {e}")
            db.session.rollback()
            return None

        return TicketMapper.entity_to_dto(ticket)

    # --- cRud ------------------------------------------------------------
    

    def find_all(self) -> list[TicketDTO]:
        # active=True: on ne montre pas les tickets désactivés (soft delete).
        return [TicketMapper.entity_to_dto(ticket)
                for ticket in Ticket.query.filter_by(active=True).order_by(Ticket.ticket_id).all()]

    def find_all_by_technician(self, technician_id: int) -> list[TicketDTO]:
        return [TicketMapper.entity_to_dto(ticket)
                for ticket in Ticket.query.filter_by(technician_id=technician_id, active=True)
                                          .order_by(Ticket.ticket_id).all()]

    def find_one(self, entity_id: int) -> TicketDTO | None:
        ticket = self.find_one_entity(entity_id)

        return TicketMapper.entity_to_dto(ticket) if ticket else None

    def find_one_entity(self, entity_id: int) -> Ticket | None:
        return Ticket.query.filter_by(ticket_id=entity_id).first()

    def find_one_by(self, **kwargs) -> Ticket | None:
        return Ticket.query.filter_by(**kwargs).first()
    
    def is_authorised(
        self,
        ticket: Ticket,
        user: UserDTO
    ) -> bool:
        return (
            ticket.author_id == user.user_id
            or ticket.technician_id == user.user_id
        )


    # --- crUd ------------------------------------------------------------

    def update(self, entity_id: int, form: TicketUpdateForm) -> TicketDTO | None:
        ticket = self.find_one_entity(entity_id)

        if ticket is None:
            return None

        TicketMapper.form_to_entity(form, ticket)

        try:
            db.session.commit()
        except Exception as e:
            app.logger.error(f"update ticket {entity_id}: {e}")
            db.session.rollback()
            return None

        return TicketMapper.entity_to_dto(ticket)

    # --- cruD ------------------------------------------------------------

    def delete(self, entity_id: int) -> int | None:
        """soft delete"""
        ticket = self.find_one_entity(entity_id)

        if ticket is None:
            return None

        ticket.soft_delete()

        try:
            db.session.commit()
        except Exception as e:
            app.logger.error(f"delete ticket {entity_id}: {e}")
            db.session.rollback()
            return None

        return ticket.ticket_id