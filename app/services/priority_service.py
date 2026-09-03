from app.dtos.priority_dto import PriorityDTO
from app.framework.decorators.injectable import injectable
from app.mappers.priority_mapper import PriorityMapper
from app.models.priority import Priority
#from app.services.base_service import BaseService


@injectable
class PriorityService():
    """Read only for the moment"""

    def find_all(self) -> list[PriorityDTO]:
        # active=True: on ne montre pas les priorités désactivées (soft delete).
        return [PriorityDTO.build_from_entity(priority)
                for priority in Priority.query.filter_by(active=True).order_by(Priority.priority_id).all()]

    def find_one(self, entity_id: int) -> PriorityDTO | None:
        priority = self.find_one_entity(entity_id)

        return PriorityDTO.build_from_entity(priority) if priority else None

    def find_one_entity(self, entity_id: int) -> Priority | None:
        return Priority.query.filter_by(priority_id=entity_id).first()

    def find_one_by(self, **kwargs) -> Priority | None:
        return Priority.query.filter_by(**kwargs).first()

    