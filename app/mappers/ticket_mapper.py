from app.dtos.ticket_dto import TicketDTO
from app.forms.ticket.ticket_create_form import TicketCreateForm
from app.forms.ticket.ticket_update_form import TicketUpdateForm
from app.mappers.abstract_mapper import AbstractMapper
from app.models.ticket import Ticket, TicketStatus


class TicketMapper(AbstractMapper):
    @staticmethod
    def entity_to_dto(entity: Ticket) -> TicketDTO:
        return TicketDTO.build_from_entity(entity)

    @staticmethod
    def form_to_entity(form, ticket: Ticket) -> Ticket:
        """Reporte les champs du formulaire sur l'entité.

        Deux formulaires, deux jeux de champs autorisés (même logique que
        UserMapper): la création ne touche ni au statut ni au technicien,
        l'édition les autorise tous les deux.
        """
        if isinstance(form, TicketCreateForm):
            ticket.ticket_title = form.ticket_title.data
            ticket.ticket_description = form.ticket_description.data or ""
            ticket.category_id = form.category_id.data
            ticket.priority_id = form.priority_id.data
            # Statut et technicien ne sont PAS des champs du formulaire de
            # création: le modèle applique déjà default=TicketStatus.NEW, et
            # technician_id reste nullable=True (non assigné à la création).

        elif isinstance(form, TicketUpdateForm):
            ticket.ticket_title = form.ticket_title.data
            ticket.ticket_description = form.ticket_description.data or ""
            ticket.category_id = form.category_id.data
            ticket.priority_id = form.priority_id.data
            ticket.ticket_status = TicketStatus[form.ticket_status.data]
            ticket.technician_id = form.selected_technician_id()

        return ticket