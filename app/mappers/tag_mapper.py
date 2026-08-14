from app.forms.tag.tag_form import TagForm
from app.mappers.abstract_mapper import AbstractMapper
from app.models.tag import Tag
from app.dtos.tag_dto import TagDTO

class TagMapper(AbstractMapper):

    @staticmethod
    def entity_to_dto(tag : Tag) -> TagDTO:
        return TagDTO.build_from_entity(tag)

    @staticmethod
    def form_to_entity(form, tag: Tag) -> Tag:
        if isinstance(form, TagForm):
            tag.tag_name = form.name
            tag.tag_color = form.color

        return tag