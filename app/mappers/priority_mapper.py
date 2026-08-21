from app.dtos.priority_dto import PriorityDTO
from app.mappers.abstract_mapper import AbstractMapper
from app.models.priority import Priority


class PriorityMapper(AbstractMapper):
    @staticmethod
    def entity_to_dto(entity: Priority) -> PriorityDTO:
        return PriorityDTO.build_from_entity(entity)

    @staticmethod
    def form_to_entity(form, priority: Priority) -> Priority:
        raise NotImplementedError("TODO : controller et form pour mettre à jours un priorité")