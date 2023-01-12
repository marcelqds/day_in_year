from datetime import datetime

class DayInYear:
    def __init__(self, year: int, month: int, day: int):
        self.__check_int(year, month, day)        
        self.__check_year(year)
        self.__check_month(month)
        self.__check_day(day)
        try:
            datetime(year,month,day)
        except:
            raise Exception('Informe uma data válida')
            
    def __check_int(self,year: int, month: int, day: int):
        if not (
            isinstance(year, int) and 
            isinstance(month, int) and 
            isinstance(day, int)
        ):
            raise Exception('O ano, mes, e dia devem ser inteiro')

    def __check_year(self,year: int):
        if not year > 1969:
            raise Exception('O ano deve ser maior que 1969.')

    def __check_month(self,month: int):
        if not (month > 0 and month < 13):
            raise Exception('O mês deve ser de 1 a 12.')

    def __check_day(self,day: int):
        if not (day > 0 and day < 32):
            raise Exception('O dia deve ser de 1 a 31')

    
        
        
    

    