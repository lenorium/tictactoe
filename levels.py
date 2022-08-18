from enum import Enum


class Levels(Enum):
    USER = 'user'
    EASY = 'easy'
    MEDIUM = 'medium'

    @classmethod
    def is_level(cls, level):
        return level in [level.value for level in cls]
