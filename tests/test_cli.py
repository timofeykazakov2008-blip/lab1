from __future__ import annotations

import subprocess
import sys


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    """Run CLI command as subprocess"""
    return subprocess.run(
        [sys.executable, "-m", "toolkit", *args],
        capture_output=True,
        text=True,
        check=False,
    )

def test_cli_help() -> None:
    """Test --help flag exits with code 0"""
    res = run_cli("--help")
    assert res.returncode == 0
    assert "calc" in res.stdout

def test_cli_calc() -> None:
    """Test basic calculation in CLI"""
    res = run_cli("calc", "2 + 2")
    assert res.returncode == 0
    assert res.stdout.strip() == "4"

def test_cli_RPN_flag() -> None:
    """Test calc with --RPN flag"""
    res = run_cli("calc", "--RPN", "2 + 3 * 5")
    assert res.returncode == 0
    assert res.stdout.strip() == "2 3 5 * +"

def test_cli_convert() -> None:
    """Test valid unit conversion in CLI"""
    res = run_cli("convert", "1000", "--from", "mm", "--to", "m")
    assert res.returncode == 0
    assert res.stdout.strip() == "1"

def test_cli_calc_delzero() -> None:
    """Test division by zero exits with code 2"""
    res = run_cli("calc", "10 / 0")
    assert res.returncode == 2
    assert "ERROR:" in res.stderr

def test_cli_convert_different_group() -> None:
    """Test incompatible units exit with code 2"""
    res = run_cli("convert", "10", "--from", "kg", "--to", "m")
    assert res.returncode == 2
    assert "ERROR:" in res.stderr

def test_cli_unknown() -> None:
    """Test unknown command exits with code 2"""
    res = run_cli("67LETSGO67")
    assert res.returncode == 2
    assert "ERROR:" in res.stderr

def test_cli_empty() -> None:
    """Test running without arguments exits with code 2"""
    res = run_cli()
    assert res.returncode == 2
    assert "ERROR:" in res.stderr
