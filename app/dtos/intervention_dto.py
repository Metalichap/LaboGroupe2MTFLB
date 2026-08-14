from app.dtos.abstract_dto import AbstractDTO
from app.models.intervention import Intervention

class InterventionDTO(AbstractDTO):

    def __init__(self):
        self.intervention_id = None
        self.intervention_date = None
        self.intervention_duration = None
        self.intervention_report = None
        self.ticket_id = None
        self.technician_id = None
        self.interventiontype_id = None

    @staticmethod
    def build_from_entity(inter : Intervention) -> "InterventionDTO" :
        inter_dto = InterventionDTO()

        inter_dto.intervention_id = inter.intervention_id
        inter_dto.intervention_date = inter.intervention_date
        inter_dto.intervention_duration = inter.intervention_duration
        inter_dto.intervention_report = inter.intervention_report
        inter_dto.ticket_id = inter.ticket_id
        inter_dto.technician_id = inter.technician_id
        inter_dto.interventiontype_id = inter.interventiontype_id

        return inter_dto

    def get_json_parsable(self):
        return self.__dict__