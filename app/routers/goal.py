from enum import Enum

class GoalType(Enum):
    HABIT = 'habit'
    MILESTONE = 'milestone'

class Goal:
    def __init__(self, goal_id, goal_type, title, description, progress, archived=False, completed=False):
        self.id = goal_id
        self.type = goal_type
        self.title = title
        self.description = description
        self.progress = progress
        self.archived = archived
        self.completed = completed
