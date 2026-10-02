from __future__ import annotations

import pytest

from toolkit.__main__ import form_expression
from toolkit.calculator import RPN, calculate, token, validate
from toolkit.errors import CalculatorError


def test_calculate_sum() -> None:
    """Test +"""
    res = calculate('2 + 2')
    assert res == 4.0

def test_calculate_minus() -> None:
    """Test -"""
    res = calculate('5 - 3')
    assert res == 2.0

def test_calculate_mul() -> None:
    """Test *"""
    res = calculate('6 * 6')
    assert res == 36.0

def test_calculate_del() -> None:
    """Test /"""
    res = calculate('18 / 9')
    assert res == 2.0

def test_calculate_operators() -> None:
    """Test +*"""
    res = calculate('2 + 2 * 5')
    assert res == 12.0

def test_calculate_minus_numbers() -> None:
    """Test -numbers"""
    res = calculate('-5 + 10')
    assert res == 5.0

def test_calculate_float() -> None:
    """Test float numbers"""
    res = calculate('2.3 + 3.75')
    assert res == 6.05

def test_calculate_rpn() -> None:
    """Test convertion to RPN"""
    tokens = token('17 + 18 * 3')
    valid = validate(tokens)
    rpn = RPN(valid)
    res = form_expression(rpn)
    assert res == "17 18 3 * +"

def test_calculate_del_zero() -> None:
    """Test / 0"""
    with pytest.raises(CalculatorError):
        calculate('25 / 0')

def test_calculate_invalid_simvol() -> None:
    """Test invalid simvol in expression"""
    with pytest.raises(CalculatorError):
        calculate('18 + a - 9')

def test_calculate_excess_operators() -> None:
    """Test excess operators in expression"""
    with pytest.raises(CalculatorError):
        calculate('18 +* 9')
