import re
from typing import List

from Helpers.flower_helper import FlowerHelper
from Helpers.size_helper import SizeHelper
from Models.bouquet_design import BouquetDesign

total_quantity_regex = re.compile(r'\d+$')


class BouquetDesignHelper:
    @staticmethod
    def get_bouquet_design(raw_bouquet_design: str) -> BouquetDesign:
        bouquet_name = raw_bouquet_design[0].upper()
        bouquet_size = SizeHelper.get_size(raw_bouquet_design[1])

        flowers = FlowerHelper.get_flower_bunches(raw_bouquet_design)

        total_quantity = re.search(total_quantity_regex, raw_bouquet_design)
        total_quantity = int(total_quantity[0])

        return BouquetDesign(bouquet_name, bouquet_size, flowers, total_quantity)

    @staticmethod
    def get_bouquet_designs(raw_bouquet_designs) -> List[BouquetDesign]:
        bouquet_designs = []

        for raw_bouquet_design in raw_bouquet_designs:
            bouquet_design = BouquetDesignHelper.get_bouquet_design(raw_bouquet_design)
            bouquet_designs.append(bouquet_design)

        return bouquet_designs
