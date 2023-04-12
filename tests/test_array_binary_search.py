from array_binary_search.array_binary_search import binary_search
import pytest

def test_array() :
    actual =  binary_search([4, 8, 15, 16, 23, 42], 15)
    excepted = 2
    assert actual == excepted

def test_array2() :
    actual =  binary_search([-131, -82, 0, 27, 42, 68, 179], 42)
    excepted = 4
    assert actual == excepted    

def test_array3() :
    actual =  binary_search([11, 22, 33, 44, 55, 66, 77], 90)
    excepted = -1
    assert actual == excepted 
   
def test_array4() :
    actual =  binary_search([1, 2, 3, 5, 6, 7], 4)
    excepted = -1
    assert actual == excepted 
    