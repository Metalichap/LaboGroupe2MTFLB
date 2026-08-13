from app.dtos.tag_dto import TagDTO
from app.forms.tag.tag_form import TagForm
from app.mappers.tag_mapper import TagMapper
from app.services.base_service import BaseService
from app.framework.decorators.injectable import injectable
from app.models.tag import Tag
from app import app, db


@injectable
class TagService(BaseService):

    def find_all(self) -> list[TagDTO]:
        return [TagMapper.entity_to_dto(tag) for tag in self.find_all_entities()]

    def find_all_entities(self) -> list[Tag]:
        return Tag.query.order_by(Tag.tag_id).all()

    def find_one(self, entity_id: int) -> TagDTO | None:
        tag = self.find_one_entity(entity_id)

        return TagMapper.entity_to_dto(tag) if tag else None

    def find_one_entity(self, entity_id: int) -> Tag | None:
        return Tag.query.filter_by(tag_id=entity_id).first()

    def find_one_by(self, **kwargs) -> Tag | None:
        return Tag.query.filter_by(**kwargs).first()



    def insert(self, form: TagForm):
        tag = Tag()
        TagMapper.form_to_entity(form, tag)

        try :
            db.session.add(tag)
            db.session.commit()
        except Exception as e :
            app.logger.error(f"insert tag: {e}")
            db.session.rollback()
            return None

        return TagMapper.entity_to_dto(tag)


    def update(self, entity_id: int, form : TagForm):
        tag = self.find_one_entity(entity_id)

        if tag is None:
            return None

        TagMapper.form_to_entity(form, tag)

        try :
            db.session.commit()
        except Exception as e:
            app.logger.error(f"update tag {entity_id}: {e}")
            db.session.rollback()
            return None

        return TagMapper.entity_to_dto(tag)

    def delete(self, entity_id: int):
        tag = self.find_one_entity(entity_id)

        if tag is None:
            return None

        tag.soft_delete()

        try :
            db.session.commit()
        except Exception as e:
            app.logger.error(f"delete tag {entity_id}: {e}")
            db.session.rollback()
            return None

        return tag.tag_id

