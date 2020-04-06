from Models.Enums.size import Size
from Models.flower import Flower


class FlowerBunch(Flower):
    def __init__(self, specie: str, size: Size, flowers_quantity: int):
        super().__init__(specie, size)

        self.flowers_quantity: int = flowers_quantity
