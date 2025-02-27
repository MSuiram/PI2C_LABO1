import pytest
import utils

def test_fact():
    assert utils.fact(5) == 120
    assert utils.fact(-2) == None

def test_roots():
    assert utils.roots(2,-9,-5) == (-1/2,5) or (5,-1/2)
    assert utils.roots(-2,-2,-2) == ()
    assert utils.roots(8,0,0) == (0)

def test_integrate():
    assert utils.integrate('x ** 2 - 1', -1, 1) == -1.3333333333333335
    assert utils.integrate('x ** 2', -1, 1) == 2/3
