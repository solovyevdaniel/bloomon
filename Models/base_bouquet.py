from typing import List

from Models.Enums.size import Size
from Models.flower_bunch import FlowerBunch


class BaseBouquet:
    def __init__(self, name: str, size: Size, flower_bunches: List[FlowerBunch]):
        self.name: str = name
        self.size: Size = size
        self.flower_bunches: List[FlowerBunch] = flower_bunches
