from app import app, db
from app.dtos.team import TeamDTO
from app.forms.team.team_form import TeamInsertForm, TeamUpdateForm
from app.framework.decorators.injectable import injectable
from app.mappers.team_mapper import TeamMapper
from app.models.team import Team
from app.services.base_service import BaseService


@injectable
class TeamService(BaseService[TeamDTO, Team, TeamInsertForm, TeamUpdateForm]):
    """Category CRUD"""

    # --- Crud -----------------------------------------------------------

    def insert(self, form: TeamForm) -> TeamDTO | None:
        
        team = Team()
        TeamMapper.form_to_entity(form, team)

        try:
            db.session.add(team)
            db.session.commit()
        except Exception as e:
            # log error
            app.logger.error(f"insert category: {e}")
            db.session.rollback()
            return None

        return TeamMapper.entity_to_dto(team)

    # --- cRud ------------------------------------------------------------

    def find_all(self) -> list[TeamDTO]:
        # active=True. Filter out soft delete
        return [TeamMapper.entity_to_dto(team)
                for team in Team.query.filter_by(active=True).order_by(Team.team_id).all()]
    
    def find_all_entities(self) -> list[Team]:
        """Version entités, pour les usages internes (choices d'un formulaire,
        attribution d'un rôle à un user...)."""
        return Team.query.order_by(Team.team_id).all()

    def find_one(self, entity_id: int) -> TeamDTO | None:
        team = self.find_one_entity(entity_id)

        return TeamMapper.entity_to_dto(team) if team else None

    def find_one_entity(self, entity_id: int) -> Team | None:
        return Team.query.filter_by(category_id=entity_id).first()

    def find_one_by(self, **kwargs) -> Team | None:
        return Team.query.filter_by(**kwargs).first()
    

    # --- crUd ------------------------------------------------------------

    def update(self, entity_id: int, form: TeamForm) -> TeamDTO | None:
        
        team = self.find_one_entity(entity_id)

        if team is None:
            return None

        TeamMapper.form_to_entity(form, team)

        try:
            db.session.commit()
        except Exception as e:
            # log error
            app.logger.error(f"update category {entity_id}: {e}")
            db.session.rollback()
            return None

        return TeamMapper.entity_to_dto(team)
    

    # --- cruD ------------------------------------------------------------

    def delete(self, entity_id: int) -> int | None:
        """soft delete: la catégorie est désactivée

        """
        team = self.find_one_entity(entity_id)

        if team is None:
            return None

        team.soft_delete()

        try:
            db.session.commit()
        except Exception as e:
            # log error
            app.logger.error(f"delete category {entity_id}: {e}")
            db.session.rollback()
            return None

        return team.team_id