from app.dtos.abstract_dto import AbstractDTO
from app.models.tag import Tag


class TagDTO(AbstractDTO) :
    def __init__(self):
        self.tag_id = None
        self.tag_name = None
        self.tag_color = None

    @staticmethod
    def build_from_entity(tag: Tag) -> "TagDTO" :
        tag_dto = TagDTO()

        tag_dto.tag_id = Tag.tag_id
        tag_dto.tag_name = Tag.tag_name
        tag_dto.tag_color = Tag.tag_color

        return tag_dto

    def get_json_parsable(self):

        return self.__dict__

