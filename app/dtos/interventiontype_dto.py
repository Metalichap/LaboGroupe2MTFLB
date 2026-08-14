from app.dtos.abstract_dto import AbstractDTO
from app.models.interventiontype import InterventionType

class InterventionTypeDTO(AbstractDTO):

    def __init__(self):
        self.interventiontype_id = None
        self.interventiontype_name = None
        self.interventiontype_description = None

    @staticmethod
    def build_from_entity(interType : InterventionType) -> "InterventionTypeDTO":
        itype_dto = InterventionTypeDTO()

        itype_dto.interventiontype_id = interType.interventiontype_id
        itype_dto.interventiontype_name = interType.interventiontype_name
        itype_dto.interventiontype_description = interType.interventiontype_description

        return itype_dto

    def get_json_parsable(self):
        return self.__dict__