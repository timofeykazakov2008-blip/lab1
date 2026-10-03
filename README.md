Лабораторная работа номер 1
Структура проекта
`src/toolkit/calculator.py` — токенизация, валидация и вычисление выражений, через стеки
`src/toolkit/converter.py` — перевод единиц длины, массы и температуры.
`src/toolkit/errors.py` — кастомные исключения ядра (`CalculatorError`, `ConverterError`).
`src/toolkit/constants.py` — коэффициенты и словари единиц измерения.
`src/toolkit/__main__.py` — точка входа CLI.
`tests/` — модульные тесты для ядра и CLI.
Клонирование репазитория:
```bash
git clone <URL_ВАШЕГО_РЕПОЗИТОРИЯ>
cd lab1

Установка и запуск
1. Создание и активация виртуального окружения:
```bash
python3.12 -m venv .venv
source .venv/bin/activate

2. Установка зависимостей:
pip install -r requirements.txt

3. Запуск:
# Калькулятор
python -m toolkit calc "expression"
# Перевод выражение в постфиксную запись
python -m toolkit calc --RPN "expression"
# Конвертер величин
python -m toolkit convert VALUE --from UNIT --to UNIT
# Справка/помощь
python -m tookit --help

Тестирование проекта

pytest -v
ruff check .
mypy src/toolkit
