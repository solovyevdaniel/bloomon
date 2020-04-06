from typing import List

from Helpers.bouquet_helper import BouquetHelper
from Models.bouquet import Bouquet
from Models.bouquet_design import BouquetDesign
from Models.flower_bunch import FlowerBunch


class BouquetService:
    def __init__(self, bouquet_designs: List[BouquetDesign], available_flower_bunches: List[FlowerBunch]):
        self.bouquet_designs = bouquet_designs
        self.available_flower_bunches = available_flower_bunches

    def collect_bouquets(self) -> List[Bouquet]:
        bouquets = []

        for bouquet_design in self.bouquet_designs:
            bouquet = self.collect_bouquet(bouquet_design)

            if not bouquet.is_ready:
                bouquet = self.add_extra_flowers_to_bouquet(bouquet, bouquet_design)

            bouquets.append(bouquet)

        return bouquets

    def collect_bouquet(self, bouquet_design: BouquetDesign) -> Bouquet:
        collected_flower_bunches = []

        for flower_bunch in bouquet_design.flower_bunches:
            appropriate_flower_bunch = list(filter(lambda x: ((x.size == flower_bunch.size)
                                                              and (x.specie == flower_bunch.specie)),
                                                   self.available_flower_bunches))
            if appropriate_flower_bunch:
                appropriate_flower_bunch = appropriate_flower_bunch[0]

                if appropriate_flower_bunch.flowers_quantity >= flower_bunch.flowers_quantity:
                    appropriate_flower_bunch.flowers_quantity -= flower_bunch.flowers_quantity
                    bouquet_flower_bunch = FlowerBunch(flower_bunch.specie,
                                                       flower_bunch.size,
                                                       flower_bunch.flowers_quantity)
                    collected_flower_bunches.append(bouquet_flower_bunch)

        bouquet = Bouquet(bouquet_design.name, bouquet_design.size, collected_flower_bunches)
        bouquet.current_total_flowers_quantity = sum(q.flowers_quantity for q in bouquet.flower_bunches)

        bouquet.is_ready = BouquetHelper.check_is_ready(bouquet, bouquet_design)

        return bouquet

    def add_extra_flowers_to_bouquet(self, bouquet: Bouquet, bouquet_design: BouquetDesign) -> Bouquet:
        used_species = {f.specie for f in bouquet.flower_bunches}

        for available_flower_bunch in self.available_flower_bunches:
            if bouquet.is_ready:
                break
            else:
                need_extra_quantity = bouquet_design.expected_total_flowers_quantity - bouquet.current_total_flowers_quantity

                if ((available_flower_bunch.flowers_quantity >= need_extra_quantity)
                        and (available_flower_bunch.size == bouquet.size)
                        and (available_flower_bunch.specie not in used_species)):

                    flower_bunch = FlowerBunch(available_flower_bunch.specie,
                                               available_flower_bunch.size,
                                               need_extra_quantity)
                    bouquet.flower_bunches.append(flower_bunch)

                    bouquet.current_total_flowers_quantity = sum(q.flowers_quantity for q in bouquet.flower_bunches)
                    bouquet.is_ready = BouquetHelper.check_is_ready(bouquet, bouquet_design)

        return bouquet
