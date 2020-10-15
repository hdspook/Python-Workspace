import math
from fact import fact
import pytest

def test_fact():
    num = 25
    assert math.factorial(num) == fact(num)

def test_zero():
    with pytest.raises(ZeroDivisionError):
        1/0

def testsquare():
    num = 7
    assert 7*7 == 40




