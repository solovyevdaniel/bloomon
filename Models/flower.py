from Models.Enums.size import Size


class Flower:
    def __init__(self, specie: str, size: Size):
        self.specie: str = specie
        self.size: Size = size
