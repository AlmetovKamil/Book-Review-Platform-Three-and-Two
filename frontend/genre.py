from enum import Enum


class Genre(str, Enum):
    fiction = 'fiction'
    science = 'science'