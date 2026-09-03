from app.dtos.commands.category_command import CategoryCommand
from app.forms.category.category_form import CategoryForm


class CategoryMapper:
    @staticmethod
    def form_to_command(form: CategoryForm) -> CategoryCommand:
        return CategoryCommand(
            category_name=form.category_name.data,
            category_description=form.category_description.data
        )