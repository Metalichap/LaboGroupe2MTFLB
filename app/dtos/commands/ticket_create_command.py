from dataclasses import dataclass


@dataclass
class TicketCreateCommand:
    ticket_title: str
    ticket_description: str
    category_id: int
    priority_id: int

    def apply_to_entity(self, ticket):
        ticket.ticket_title = self.ticket_title
        ticket.ticket_description = self.ticket_description or ""
        ticket.category_id = self.category_id
        ticket.priority_id = self.priority_id
        
        return ticket