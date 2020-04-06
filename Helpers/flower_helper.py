import re
from itertools import groupby
from typing import List

from Helpers.size_helper import SizeHelper
from Models.flower import Flower
from Models.flower_bunch import FlowerBunch

flowers_regex = re.compile(r'(?:\d+[a-z])')


class FlowerHelper:
    @staticmethod
    def get_flower_bunches(raw_bouquet_design: str) -> List[FlowerBunch]:
        raw_flowers = re.findall(flowers_regex, raw_bouquet_design)
        flower_size = SizeHelper.get_size(raw_bouquet_design[1])
        flowers = []

        for f in raw_flowers:
            specie = f[-1]
            quantity = int(f[:-1])
            flowers.append(FlowerBunch(specie, flower_size, quantity))

        return flowers

    @staticmethod
    def get_flower(raw_flower: str) -> Flower:
        specie = raw_flower[0].lower()
        size = SizeHelper.get_size(raw_flower[1])
        return Flower(specie, size)

    @staticmethod
    def get_flowers(raw_flowers) -> List[Flower]:
        flowers = []
        for raw_available_flower in raw_flowers:
            flower = FlowerHelper.get_flower(raw_available_flower)
            flowers.append(flower)

        return flowers

    @staticmethod
    def get_available_flower_bunches(flowers: List[Flower]) -> List[FlowerBunch]:
        flower_bunches = []
        sorted_flowers = sorted(flowers, key=lambda x: (x.specie, x.size.value))
        for (specie, size_str), groupped_flowers in groupby(sorted_flowers,
                                                            key=lambda x: (x.specie, x.size.value)):
            groupped_flowers = [f for f in groupped_flowers]
            flowers_quantity = len(groupped_flowers)
            size = SizeHelper.get_size(size_str)

            flower_bunch = FlowerBunch(specie, size, flowers_quantity)
            flower_bunches.append(flower_bunch)

        return flower_bunches
