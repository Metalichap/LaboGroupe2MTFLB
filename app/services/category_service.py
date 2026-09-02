from app import app, db
from app.dtos.category_dto import CategoryDTO
from app.dtos.commands.category_command import CategoryCommand
from app.framework.decorators.injectable import injectable
from app.models.category import Category
from app.services.base_service import BaseService


@injectable
class CategoryService(BaseService):

    # --- Crud -----------------------------------------------------------

    def insert(self, command: CategoryCommand) -> CategoryDTO | None:

        category = command.apply_to_entity(Category())

        try:
            db.session.add(category)
            db.session.commit()
        except Exception as e:
            app.logger.error(f"insert category: {e}")
            db.session.rollback()
            return None

        return CategoryDTO.build_from_entity(category)



    # --- cRud ------------------------------------------------------------

    def find_all(self) -> list[CategoryDTO]:
        return [CategoryDTO.build_from_entity(category)
                for category in Category.query.filter_by(active=True).order_by(Category.category_id).all()]

    def find_one(self, entity_id: int) -> CategoryDTO | None:
        category = self.find_one_entity(entity_id)

        return CategoryDTO.build_from_entity(category) if category else None

    def find_one_entity(self, entity_id: int) -> Category | None:
        return Category.query.filter_by(category_id=entity_id).first()

    def find_one_by(self, **kwargs) -> Category | None:
        return Category.query.filter_by(**kwargs).first()
    

    # --- crUd ------------------------------------------------------------

    def update(self, entity_id: int, command: CategoryCommand) -> CategoryDTO | None:

        category = self.find_one_entity(entity_id)

        if category is None:
            return None

        command.apply_to_entity(category)

        try:
            db.session.commit()
        except Exception as e:
            app.logger.error(f"update category {entity_id}: {e}")
            db.session.rollback()
            return None

        return CategoryDTO.build_from_entity(category)
    

    # --- cruD ------------------------------------------------------------

    def delete(self, entity_id: int) -> int | None:
        """Suppression logique (soft delete)."""
        category = self.find_one_entity(entity_id)

        if category is None:
            return None

        category.soft_delete()

        try:
            db.session.commit()
        except Exception as e:
            app.logger.error(f"delete category {entity_id}: {e}")
            db.session.rollback()
            return None

        return category.category_id