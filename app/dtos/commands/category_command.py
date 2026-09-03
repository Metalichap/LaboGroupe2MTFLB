from dataclasses import dataclass

@dataclass
class CategoryCommand:
    category_name: str
    category_description: str

    def apply_to_entity(self, category):
        category.category_name = self.category_name
        category.category_description = self.category_description or ""

        return category
    

