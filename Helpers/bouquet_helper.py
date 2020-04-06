from Models.bouquet import Bouquet
from Models.bouquet_design import BouquetDesign


class BouquetHelper:
    @staticmethod
    def check_is_ready(bouquet: Bouquet, bouquet_design: BouquetDesign) -> bool:
        if bouquet.current_total_flowers_quantity == bouquet_design.expected_total_flowers_quantity:
            return True

        return False
