from toolkit.constants import ABSOLUTE_0, LENGTH, MASSA
from toolkit.errors import ConverterError


def conv_temperature(znach: float, vel1: str, vel2: str) -> float:
    """Вспомогательная функция дял перевода температур, здесь описаны и выполненны все возможные действия с температурами"""
    if znach < ABSOLUTE_0[vel1]:
        raise ConverterError('Температура ниже абсолютного нуля.')
    elif vel1 == vel2:
        return(znach)
    elif vel1 == 'c' and vel2 == 'f':
        return(znach * 1.8 + 32)
    elif vel1 == 'c' and vel2 == 'k':
        return(znach + 273.15)
    elif vel1 == 'f' and vel2 == 'c':
        return((znach - 32)/1.8)
    elif vel1 == 'k' and vel2 == 'c':
        return(znach - 273.15)
    elif vel1 == 'f' and vel2 == 'k':
        return((znach - 32)/1.8 + 273.15)
    elif vel1 == 'k' and vel2 == 'f':
        return((znach-273.15)*1.8 + 32)
    else:
        raise ConverterError('Недопустиая величина конвертации.')

def convert(znach: float, vel1: str, vel2: str) -> float:
    """Конвертацяи чисел, если мы переводим массу и длинну мы пользуемся данными из файла constants где у нас есть
    базовая велична, через которую происходят все вычисления, переводя температуры мы пользумеся вспомогательной функцией"""
    vel1 = vel1.lower()
    vel2 = vel2.lower()
    if vel1 not in MASSA and vel1 not in LENGTH and vel1 not in ABSOLUTE_0:
        raise ConverterError(f"Неизвестная единица измерения: '{vel1}'")
    elif vel2 not in MASSA and vel2 not in LENGTH and vel2 not in ABSOLUTE_0:
        raise ConverterError(f"Неизвестная единица измерения: '{vel2}'")
    elif vel1 in MASSA and vel2 in MASSA:
        return((znach * MASSA[vel1]) / MASSA[vel2])
    elif vel1 in LENGTH and vel2 in LENGTH:
        return((znach * LENGTH[vel1]) / LENGTH[vel2])
    elif vel1 in ABSOLUTE_0 and vel2 in ABSOLUTE_0:
        return(conv_temperature(znach, vel1, vel2))
    else:
        raise ConverterError('Конвертация между разными группами величин.')
