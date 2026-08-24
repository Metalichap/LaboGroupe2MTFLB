from app.dtos.team_dto import TeamDTO
from app.forms.team.team_form import TeamInsertForm
from app.mappers.abstract_mapper import AbstractMapper
from app.models.team import Team

class TeamMapper(AbstractMapper[TeamDTO, Team, TeamInsertForm]):
    @staticmethod
    def entity_to_dto(entity: Team) -> TeamDTO:
        return TeamDTO.build_from_entity(entity)

    @staticmethod
    def form_to_entity(form: TeamInsertForm, entity: Team) -> Team:

        entity.team_name = form.team_name.data
        entity.team_description = form.team_description.data or ""

        return entity