from app import app, db
from app.models.intervention import Intervention
from app.framework.decorators.injectable import injectable
from app.services.base_service import BaseService
from app.mappers.intervention_mapper import InterventionMapper
from app.forms.intervention.intervention_form import InterventionForm
from app.dtos.intervention_dto import InterventionDTO


@injectable
class InterventionService(BaseService):

    def find_all(self) -> list[InterventionDTO]:
        return [InterventionMapper.entity_to_dto(inter) for inter in self.find_all_entities()]

    def find_all_entities(self) -> list[Intervention]:
        return Intervention.query.order_by(Intervention.intervention_id).all()

    def find_one(self, entity_id: int) -> InterventionDTO | None:
        inter = self.find_one_entity(entity_id)
        return InterventionMapper.entity_to_dto(inter) if inter else None

    def find_one_entity(self, entity_id: int) -> Intervention | None:
        return Intervention.query.filter_by(intervention_id=entity_id).first()

    def find_one_by(self, **kwargs) -> Intervention | None:
        return Intervention.query.filter_by(**kwargs).first()

    def insert(self, form: InterventionForm) -> InterventionDTO | None:
        inter = Intervention()
        InterventionMapper.form_to_entity(form, inter)

        try:
            db.session.add(inter)
            db.session.commit()
        except Exception as e:
            app.logger.error(f"insert intervention : {e}")
            db.session.rollback()
            return None

        return InterventionMapper.entity_to_dto(inter)

    def update(self, entity_id: int, form: InterventionForm) -> InterventionDTO | None:
        inter = self.find_one_entity(entity_id)

        if inter is None:
            return None

        InterventionMapper.form_to_entity(form, inter)

        try:
            db.session.commit()
        except Exception as e:
            app.logger.error(f"update intervention {entity_id}: {e}")
            db.session.rollback()
            return None

        return InterventionMapper.entity_to_dto(inter)

    def delete(self, entity_id: int) -> int | None:
        inter = self.find_one_entity(entity_id)

        if inter is None:
            return None

        inter.soft_delete()

        try:
            db.session.commit()
        except Exception as e:
            app.logger.error(f"delete intervention {entity_id}: {e}")
            db.session.rollback()
            return None

        return inter.intervention_id
