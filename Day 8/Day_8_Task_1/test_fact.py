import math
from fact import fact

def test_fact():
    num = 25
    assert math.factorial(num) == fact(num)

def testsquare():
    num = 7
    assert 7*7 == 40


