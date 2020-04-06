from typing import List

from Models.Enums.size import Size
from Models.base_bouquet import BaseBouquet
from Models.flower_bunch import FlowerBunch


class BouquetDesign(BaseBouquet):
    def __init__(self, name, size: Size, flower_bunches: List[FlowerBunch], total_quantity: int):
        super().__init__(name, size, flower_bunches)

        self.expected_total_flowers_quantity: int = total_quantity
