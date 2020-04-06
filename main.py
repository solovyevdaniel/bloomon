from Helpers.bouquet_design_helper import BouquetDesignHelper
from Helpers.flower_helper import FlowerHelper
from Services.bouquet_service import BouquetService


def read_data_from_file():
    with open('sample.txt') as f:
        return [row.strip() for row in f.readlines()]


def get_separator_index(data, separator) -> int:
    return data.index(separator)


def main():
    data = read_data_from_file()
    separator_index = get_separator_index(data, '')
    raw_bouquet_designs = data[:separator_index]
    raw_flowers = data[separator_index+1:]

    bouquet_designs = BouquetDesignHelper.get_bouquet_designs(raw_bouquet_designs)
    flowers = FlowerHelper.get_flowers(raw_flowers)
    available_flower_bunches = FlowerHelper.get_available_flower_bunches(flowers)

    bouquet_service = BouquetService(bouquet_designs, available_flower_bunches)
    bouquets = bouquet_service.collect_bouquets()

    # todo here should be output method with alphabetic


if __name__ == '__main__':
    main()
