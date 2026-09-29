from __future__ import annotations

from toolkit.constants import OPERATORS
from toolkit.errors import CalculatorError

PRIORITY: dict[str,int] = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
}
def token(expression: str) -> list[str]:
    tokens = []
    i = 0
    if not expression.strip():
        raise CalculatorError('Пустое выражение.')
    while i < len(expression):
        if expression[i] == ' ':
            i+=1
        elif expression[i] in OPERATORS:
            tokens.append(expression[i])
            i+=1
        elif expression[i] in '0123456789.':
            timetokens = []
            while i < len(expression) and expression[i] in '0123456789.':
                timetokens.append(expression[i])
                i+=1
            tokens.append(''.join(timetokens))
        else:
            raise CalculatorError(f"Недопустимый символ: '{expression[i]}'.")
    return tokens
def validate(tokens: list[str]) -> list[str | float]:
    flag = True
    itog: list[str | float] = []
    unar = 1.0
    for i in tokens:
        if flag:
            if i in '+-':
                if i == '-':
                    unar *= -1.0
                continue
            if i in '*/':
                raise CalculatorError(f"Пропущено число или цифар перед оператором '{i}'.")
            try:
                num = float(i) * unar
                itog.append(num)
            except ValueError:
                raise CalculatorError(f"Неверное числовое значение: '{i}'.")
            flag = False
            unar = 1.0
        else:
            if i in OPERATORS:
                itog.append(i)
                flag = True
            else:
                raise CalculatorError(f"Пропущен оператор (+/-*) перед числом '{i}'.")
    if flag:
        raise CalculatorError('Выражение не может заканчивается оператором (+/-*).')
    return itog
def RPN(itog: list[str | float]) -> list[str | float]:
    vvod: list[str | float] = []
    stack: list[str] = []
    for i in itog:
        if i in OPERATORS:
            op = str(i)
            while stack and PRIORITY[stack[-1]] >= PRIORITY[op]:
                vvod.append(stack.pop())
            stack.append(op)
        else:
            vvod.append(i)
    while stack:
        vvod.append(stack.pop())
    return vvod
def cal_RPN(vvod: list[str | float]) -> float:
    stack: list[float] = []
    for i in vvod:
        if i not in OPERATORS:
            stack.append(float(i))
        else:
            b = stack.pop()
            a = stack.pop()
            cnt = 0.0
            if i == '+':
                cnt = a + b
            if i == '*':
                cnt = a * b
            if i == '/':
                if b == 0:
                    raise CalculatorError('Деление на ноль.')
                cnt = a / b
            if i == '-':
                cnt = a - b
            stack.append(float(cnt))
    return stack[0]
def calculate(expression: str) -> float:
    tokens = token(expression)
    itog = validate(tokens)
    vvod = RPN(itog)
    return cal_RPN(vvod)
