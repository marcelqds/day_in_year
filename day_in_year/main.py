"""Retorna o dia no ano a partir da data informada."""

from datetime import datetime


class DayInYear():
    """Class DayInYear.

        Args
            year: int 
            month: int
            day: int

        property
            date_in_the_year_to_int: -> int
    """

    def __init__(self, year: int, month: int, day: int):
        self.__check_int(year, month, day)
        self.__check_year(year)
        self.__check_month(month)
        self.__check_day(day)

        self.year = year
        self.month = month
        self.day = day

        try:
            self.date_end = datetime(year, month, day)
        except Exception as error:
            raise Exception('Informe uma data válida') from error

    def __check_int(self, year: int, month: int, day: int):
        if not (
            isinstance(year, int) and
            isinstance(month, int) and
            isinstance(day, int)
        ):
            raise Exception('O ano, mes, e dia devem ser inteiro')

    def __check_year(self, year: int):
        if year <= 1969:
            raise Exception('O ano deve ser maior que 1969.')

    def __check_month(self, month: int):
        if 1 < month > 12:
            raise Exception('O mês deve ser de 1 a 12.')

    def __check_day(self, day: int):
        if 1 < day > 31:
            raise Exception('O dia deve ser de 1 a 31')

    @property
    def date_in_the_year_to_int(self) -> int:
        """Retorna o um inteiro representando o dia no ano."""

        time_start = datetime(self.year - 1, 12, 31).timestamp()
        time_end = self.date_end.timestamp()
        days = (time_end - time_start) // (60 * 60 * 24)
        return days
