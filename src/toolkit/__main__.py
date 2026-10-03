from __future__ import annotations

import sys

from toolkit.calculator import RPN, calculate, token, validate
from toolkit.converter import convert
from toolkit.errors import ToolkitError


def form_itog(val: float) -> str:
    """Функция для избавления из числа лишних 0, например в числе 1.0 = 1"""
    if val.is_integer():
        return str(int(val))
    return str(val)

def form_expression(vvod: list[str | float]) -> str:
    """Функция для нормальнаго вывода выражений с флагом --RPN"""
    i = [form_itog(x) if isinstance(x, float) else str(x) for x in vvod]
    return " ".join(i)

def Phelp() -> None:
    """Функция вывода справки пользователю"""
    text_help = (
        'Помощь в использовании программы:\n'
        ' python -m toolkit calc [--RPN] "выражение/expression" (флаг --RPN нужен для вывода постфиксной записи выражения)\n'
        ' python -m toolkit convert VALUE --from UNIT --to UNIT\n'
        )
    sys.stdout.write(text_help)
    sys.exit(0)

def main() -> None:
    """Основная функция работы всей програмы, пользуясь sys я разбиваю получаемое выражение от пользователя на список с индексами
    так if sys.argv < 2 нам нужен чтоб понять, что пользователь не написали ничего после python -m. В функции рассматриваются 4 случая
    sys.argv и 1 вспомогательный для calculator с флагом --RPN. Когда программа понимает, ныжный вариант, то делает заданные действия
    и выводит знак завершения пргграммы 0 - успех 2 - неудача"""
    if len(sys.argv) < 2:
        sys.stderr.write('ERROR: Не указана команда. Используйте --help для справки и помощи.\n')
        sys.exit(2)
    command = sys.argv[1]
    if command in ('--help','-help','-h'):
        Phelp()
    elif command == 'calc' and (len(sys.argv) == 3 or len(sys.argv) == 4):
        try:
            if len(sys.argv) == 3:
                expression = sys.argv[2]
                res = calculate(expression)
                sys.stdout.write(f'{form_itog(res)}\n')
                sys.exit(0)
            elif len(sys.argv) == 4 and sys.argv[2] == '--RPN':
                expression = sys.argv[3]
                tokens = token(expression)
                itog = validate(tokens)
                vvod = RPN(itog)
                sys.stdout.write(f'{form_expression(vvod)}\n')
                sys.exit(0)
            else:
                sys.stderr.write(
                    'ERROR: Неверные параметры для команды calc\n'
                    'Используйте: calc "выражение" или calc --RPN "выражение"\n'
                )
                sys.exit(2)
        except ToolkitError as error:
            sys.stderr.write(f"ERROR: {error}\n")
            sys.exit(2)

    elif command == 'convert':
        if len(sys.argv) == 7 and sys.argv[3] == '--from' and sys.argv[5] == '--to':
            try:
                znach = float(sys.argv[2])
            except ValueError:
                sys.stderr.write('ERROR: Значение должно быть числом\n')
                sys.exit(2)
            vel1 = sys.argv[4]
            vel2 = sys.argv[6]
            try:
                sys.stdout.write(f'{form_itog(convert(znach, vel1, vel2))}\n')
                sys.exit(0)
            except ToolkitError as error:
                sys.stderr.write(f"ERROR: {error}\n")
                sys.exit(2)
        else:
            sys.stderr.write(
                'ERROR: Неверный формат команды convert\n'
                'Используйте: convert VALUE --from UNIT --to UNIT\n'
            )
            sys.exit(2)
    else:
        sys.stderr.write(f"ERROR: Неизвестная команда '{command}'.\n")
        sys.exit(2)
if __name__ == '__main__':
    main()
