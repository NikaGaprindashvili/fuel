import pytest
from fuel import convert, gauge

def test_convert_valid_input():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("7/8") == 88
    assert convert("2/2") == 100
    assert convert("0/2") == 0

def test_convert_invalid_input():
    with pytest.raises(ValueError):
        convert("a/b")
    with pytest.raises(ValueError):
        convert("1.5/2")
    with pytest.raises(ValueError):
        convert("2/0")
    with pytest.raises(ValueError):
        convert("2/1")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(2) == "2%"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
