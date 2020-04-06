from typing import List

from Models.base_bouquet import BaseBouquet
from Models.Enums.size import Size
from Models.flower_bunch import FlowerBunch


class Bouquet(BaseBouquet):
    def __init__(self, name: str, size: Size, flower_bunches: List[FlowerBunch]):
        super().__init__(name, size, flower_bunches)

        self.current_total_flowers_quantity: int = 0
        self.is_ready = False
