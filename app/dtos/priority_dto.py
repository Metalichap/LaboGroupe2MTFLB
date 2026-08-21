from app.dtos.abstract_dto import AbstractDTO
from app.models.priority import Priority


class PriorityDTO(AbstractDTO):
    def __init__(self):
        self.priority_id = None
        self.priority_name = None
        self.priority_level = None      # str: le .name de l'enum (ex: "URGENT")
        self.priority_delay_hours = None

    @staticmethod
    def build_from_entity(entity: Priority) -> "PriorityDTO":
        priority_dto = PriorityDTO()

        priority_dto.priority_id = entity.priority_id
        priority_dto.priority_name = entity.priority_name
        priority_dto.priority_level = entity.priority_level.name if entity.priority_level else None
        priority_dto.priority_delay_hours = entity.priority_delay_hours

        return priority_dto

    def get_json_parsable(self):
        # Que des types primitifs (int/str): pas d'objet imbriqué, donc pas
        # besoin de copie ni de reconstruction (voir RoleDTO).
        return self.__dict__