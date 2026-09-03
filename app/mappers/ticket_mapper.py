from app.dtos.commands.ticket_create_command import TicketCreateCommand
from app.dtos.commands.ticket_update_command import TicketUpdateCommand
from app.forms.ticket.ticket_create_form import TicketCreateForm
from app.forms.ticket.ticket_update_form import TicketUpdateForm
from app.models.ticket import TicketStatus


class TicketMapper:

    @staticmethod
    def form_to_create_command(form: TicketCreateForm) -> TicketCreateCommand:
        return TicketCreateCommand(
            ticket_title=form.ticket_title.data,
            ticket_description=form.ticket_description.data,
            category_id=form.category_id.data,
            priority_id=form.priority_id.data
        )

    @staticmethod
    def form_to_update_command(form: TicketUpdateForm) -> TicketUpdateCommand:
        return TicketUpdateCommand(
            ticket_title=form.ticket_title.data,
            ticket_description=form.ticket_description.data,
            category_id=form.category_id.data,
            priority_id=form.priority_id.data,
            ticket_status=TicketStatus[form.ticket_status.data],
            technician_id=form.selected_technician_id()
        )