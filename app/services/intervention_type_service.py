from app import app, db
from app.models.interventiontype import InterventionType
from app.dtos.interventiontype_dto import InterventionTypeDTO
from app.forms.intervention.interventiontype_form import InterventionTypeForm
from app.services.base_service import BaseService
from app.framework.decorators.injectable import injectable
from app.mappers.intervention_type_mapper import InterventionTypeMapper


@injectable
class InterventionTypeService(BaseService):

    def find_all(self) -> list[InterventionTypeDTO]:
        return [InterventionTypeMapper.entity_to_dto(inter_type) for inter_type in self.find_all_entities()]

    def find_all_entities(self) -> list[InterventionType]:
        return InterventionType.query.order_by(InterventionType.interventiontype_id).all()

    def find_one(self, entity_id: int) -> InterventionTypeDTO | None:
        inter_type = self.find_one_entity(entity_id)
        return InterventionTypeMapper.entity_to_dto(inter_type) if inter_type else None

    def find_one_entity(self, entity_id: int) -> InterventionType | None:
        return InterventionType.query.filter_by(interventiontype_id=entity_id).first()

    def find_one_by(self, **kwargs) -> InterventionType | None:
        return InterventionType.query.filter_by(**kwargs).first()

    def insert(self, form: InterventionTypeForm) -> InterventionTypeDTO | None:
        inter_type = InterventionType()
        InterventionTypeMapper.form_to_entity(form, inter_type)

        try :
            db.session.add(inter_type)
            db.session.commit()
        except Exception as e:
            app.logger.error(f"insert intervention type : {e}")
            db.session.rollback()
            return None

        return InterventionTypeMapper.entity_to_dto(inter_type)

    def update(self, entity_id: int, form : InterventionTypeForm) -> InterventionTypeDTO | None :
        inter_type = self.find_one_entity(entity_id)

        if inter_type is None:
            return None

        InterventionTypeMapper.form_to_entity(form, inter_type)

        try:
            db.session.commit()
        except Exception as e:
            app.logger.error(f"update intervention type {entity_id}: {e}")
            db.session.rollback()
            return None

        return InterventionTypeMapper.entity_to_dto(inter_type)

    def delete(self, entity_id : int) -> int | None:
        inter_type = self.find_one_entity(entity_id)

        if inter_type is None:
            return None

        inter_type.soft_delete()

        try :
            db.session.commit()
        except Exception as e:
            app.logger.error(f"delete intervention {entity_id}: {e}")
            db.session.rollback()
            return None

        return inter_type.interventiontype_id



