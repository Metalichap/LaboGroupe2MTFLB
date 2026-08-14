from app.forms.intervention.intervention_form import InterventionForm
from app.models.intervention import Intervention
from app.dtos.intervention_dto import InterventionDTO
from app.mappers.abstract_mapper import AbstractMapper


class InterventionMapper(AbstractMapper):

    @staticmethod
    def entity_to_dto(inter: Intervention) -> InterventionDTO:
        return InterventionDTO.build_from_entity(inter)

    @staticmethod
    def form_to_entity(form, inter: Intervention) -> Intervention:
        if isinstance(form, InterventionForm):
            inter.intervention_duration = form.duration
            inter.intervention_report = form.report
            inter.intervention_date = form.date # Eventually make sure it is conform for DB

        return inter
