from __future__ import annotations

import pytest

from toolkit.converter import convert
from toolkit.errors import ConverterError


def test_convert_m_to_cm() -> None:
    """Test length convertation"""
    res = convert(10.0,'m','CM')
    assert res == 1000.0

def test_convert_mm_to_m() -> None:
    """Test length convertation to meter"""
    res = convert(1000.0,'mm','m')
    assert res == 1.0

def test_convert_kg_to_g() -> None:
    """Test massa convertation"""
    res = convert(5.0,'KG','g')
    assert res == 5000.0

def test_convert_C_to_F() -> None:
    """Test temperature c->f convertation"""
    res = convert(100.0,'c','f')
    assert res == 212.0

def test_convert_K_to_C() -> None:
    """Test temperature k->c convertation"""
    res = convert(300.0,'k','C')
    assert res == pytest.approx(26.85)

def test_convert_different_group() -> None:
    """Conversion between different groups of quantities"""
    with pytest.raises(ConverterError):
        convert(67.0,'m','kg')

def test_convert_absolute_zero() -> None:
    """Test temperatures below absolute zero raise ConverterError"""
    with pytest.raises(ConverterError):
        convert(-300.0,'C','K')

def test_convert_unknown_simvol() -> None:
    """Test unknown simvol raise ConvertError"""
    with pytest.raises(ConverterError):
        convert(200.0,'MoTivation','K')
