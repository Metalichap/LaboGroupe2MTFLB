from app.dtos.category_dto import CategoryDTO
from app.forms.category.category_form import CategoryForm
from app.mappers.abstract_mapper import AbstractMapper
from app.models.category import Category


class CategoryMapper(AbstractMapper):
    @staticmethod
    def entity_to_dto(entity: Category) -> CategoryDTO:
        return CategoryDTO.build_from_entity(entity)

    @staticmethod
    def form_to_entity(form: CategoryForm, category: Category) -> Category:

        category.category_name = form.category_name.data
        category.category_description = form.category_description.data or ""

        return category