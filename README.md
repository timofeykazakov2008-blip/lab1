# Лабораторная работа 1. Консольный набор утилит

Пакет с интерфейсом командной строки (CLI), реализующий калькулятор выражений и конвертер физических величин.

## Структура проекта

- src/toolkit/calculator.py — токенизация, валидация и вычисление выражений через стек (ОПН).
- src/toolkit/converter.py — перевод единиц длины, массы и температуры.
- src/toolkit/errors.py — кастомные исключения ядра (CalculatorError, ConverterError).
- src/toolkit/constants.py — коэффициенты и словари единиц измерения.
- src/toolkit/__main__.py — точка входа CLI.
- tests/ — модульные тесты для ядра и CLI.

## Установка и запуск

1. Клонирование репозитория:
git clone <URL_РЕПОЗИТОРИЯ>
cd lab1

2. Создание и активация виртуального окружения:
python3.12 -m venv .venv
source .venv/bin/activate

3. Установка зависимостей:
pip install -r requirements.txt

4. Запуск калькулятора:
python -m toolkit calc "2 + 3 * 4"

5. Запуск с флагом вывода постфиксной записи (RPN):
python -m toolkit calc --RPN "2 + 3 * 4"

6. Запуск конвертера величин:
python -m toolkit convert 1000 --from mm --to m

7. Вызов справки:
python -m toolkit --help

## Тестирование проекта

Запуск тестов:
pytest -v

Проверка стиля кода:
ruff check .

Проверка типов:
mypy src/toolkit
