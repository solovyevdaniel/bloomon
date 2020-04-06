from Models.Enums.size import Size


class SizeHelper:
    @staticmethod
    def get_size(raw_size: str) -> Size:
        return Size(raw_size.upper())
