import pytest
from Merge_Sort.Merge_Sort import mergeSort

def test_merg_sort():
    # Test case 1
    arr = [5, 2, 8, 3, 1]
    expected = [1, 2, 3, 5,8]
    assert mergeSort(arr) == expected

def test_merg_sort_2():
    # Test case 2
    arr = [20,18,12,8,5,-2]
    expected = [-2,5,8,12,18,20]
    assert mergeSort(arr) == expected

def test_merg_sort_3():
    # Test case 3
    arr = [5,12,7,5,5,7]
    expected = [5, 5, 5, 7, 7, 12]
    assert mergeSort(arr) == expected
    
def test_merg_sort_4():
    # Test case 3
    arr = [2,3,5,7,13,11]
    expected = [2, 3, 5, 7, 11, 13]
    assert mergeSort(arr) == expected