from app.dtos.abstract_dto import AbstractDTO
from app.models.ticket import Ticket


class TicketDTO(AbstractDTO):
    def __init__(self):
        self.ticket_id = None
        self.ticket_title = None
        self.ticket_description = None
        self.ticket_status = None       # str: le .value de l'enum (ex: "nouveau")
        self.ticket_due_date = None
        self.created_at = None  #base entity

        self.author_id = None
        self.author_username = None
        self.technician_id = None
        self.technician_username = None
        self.category_id = None
        self.category_name = None
        self.priority_id = None
        self.priority_name = None

    @staticmethod
    def build_from_entity(entity: Ticket) -> "TicketDTO":
        ticket_dto = TicketDTO()

        ticket_dto.ticket_id = entity.ticket_id
        ticket_dto.ticket_title = entity.ticket_title
        ticket_dto.ticket_description = entity.ticket_description
        ticket_dto.ticket_status = entity.ticket_status.value if entity.ticket_status else None
        ticket_dto.ticket_due_date = entity.ticket_due_date
        ticket_dto.created_at = entity.created_at #base entity

        ticket_dto.author_id = entity.author_id
        ticket_dto.author_username = entity.author.username if entity.author else None
        ticket_dto.technician_id = entity.technician_id
        ticket_dto.technician_username = entity.technician.username if entity.technician else None
        ticket_dto.category_id = entity.category_id
        ticket_dto.category_name = entity.category.category_name if entity.category else None
        ticket_dto.priority_id = entity.priority_id
        ticket_dto.priority_name = entity.priority.priority_name if entity.priority else None

        return ticket_dto

    def get_json_parsable(self):
        # Que des types primitifs (int/str/datetime): pas d'objet imbriqué,
        # donc pas besoin de copie ni de reconstruction (voir RoleDTO).
        return self.__dict__