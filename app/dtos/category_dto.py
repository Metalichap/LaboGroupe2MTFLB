from app.dtos.abstract_dto import AbstractDTO
from app.models.category import Category


class CategoryDTO(AbstractDTO):
    def __init__(self):
        self.category_id = None
        self.category_name = None
        self.category_description = None

    @staticmethod
    def build_from_entity(entity: Category) -> "CategoryDTO":
        category_dto = CategoryDTO()

        category_dto.category_id = entity.category_id
        category_dto.category_name = entity.category_name
        category_dto.category_description = entity.category_description

        return category_dto

    def get_json_parsable(self):
        return self.__dict__