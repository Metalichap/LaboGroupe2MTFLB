from app.forms.intervention.interventiontype_form import InterventionTypeForm
from app.models.interventiontype import InterventionType
from app.dtos.interventiontype_dto import InterventionTypeDTO
from app.mappers.abstract_mapper import AbstractMapper


class InterventionTypeMapper(AbstractMapper):

    @staticmethod
    def entity_to_dto(inter_type: InterventionType) -> InterventionTypeDTO:
        return InterventionTypeDTO.build_from_entity(inter_type)

    @staticmethod
    def form_to_entity(form, inter_type : InterventionType) -> InterventionType:
        if isinstance(form, InterventionTypeForm):
            inter_type.interventiontype_name = form.name
            inter_type.interventiontype_description = form.description

        return inter_type
