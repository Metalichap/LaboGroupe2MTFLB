from typing import Optional, Any
from types import MappingProxyType
from app.dtos.abstract_dto import AbstractDTO
from app.models.team import Team


class TeamDTO(AbstractDTO[Team]):
    def __init__(self):
        self.team_id: Optional[int] = None
        self.team_name: Optional[str] = None
        self.team_description: Optional[str] = None

    @staticmethod
    def build_from_entity(entity: Team) -> "TeamDTO":
        team_dto = TeamDTO()

        team_dto.team_id = entity.team_id
        team_dto.team_name = entity.team_name
        team_dto.team_description = entity.team_description

        return team_dto

    def get_json_parsable(self) -> MappingProxyType[str, Any]:
        return self.__dict__