from dataclasses import dataclass
from datetime import datetime

from app.models.ticket import TicketStatus


@dataclass
class TicketUpdateCommand:
    ticket_title: str
    ticket_description: str
    ticket_status: TicketStatus
    ticket_due_date: datetime | None
    category_id: int
    priority_id: int
    technician_id: int | None

    def apply_to_entity(self, ticket):
        ticket.ticket_title = self.ticket_title
        ticket.ticket_description = self.ticket_description or ""
        ticket.ticket_status = self.ticket_status
        ticket.ticket_due_date = self.ticket_due_date
        ticket.category_id = self.category_id
        ticket.priority_id = self.priority_id
        ticket.technician_id = self.technician_id
        return ticket