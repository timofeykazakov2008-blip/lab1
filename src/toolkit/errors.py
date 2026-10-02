class ToolkitError(Exception):
    """Базовое исключение для ошибок приложения."""

class CalculatorError(ToolkitError):
    """Ошибка разбора или вычисления математического выражения."""

class ConverterError(ToolkitError):
    """Ошибка конвертации единиц измерения."""
