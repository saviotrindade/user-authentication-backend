from enum import Enum
from datetime import date, datetime


class Gender(Enum):
    MEN = "men"
    WOMAN = "woman"
    OTHER = "other"



# Utilizar em outro lugar!!!
def DateValidator(date: date):
    age = (datetime.now().date() - date).days
    
    if age < 18:
        raise ValueError('Você precisa ser maior de 18anos para se registrar.')
    return date