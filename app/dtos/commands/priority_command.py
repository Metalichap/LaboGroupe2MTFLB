from dataclasses import dataclass

@dataclass
class PriorityCommand:
    priority_name: str
    priority_description: str

    def apply_to_entity(self, priority):
        priority.priority_name = self.priority_name
        priority.priority_description = self.priority_description or ""
        priority.priority_level = self.priority_level or ""
        priority.priority_delay_hours = self.priority_delay_hours or ""

        return priority
    

