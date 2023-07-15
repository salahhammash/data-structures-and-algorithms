import pytest
from code_challeng_33.hash_left import left_join


def test_left_join_one():
    H1 = {'A': 1, 'B': 2}
    H2 = {'A': 1, 'C': 2}
    actual = left_join(H1 , H2)
    expected = {'A': [1,1], 'B': [2,"null"]}
    assert actual == expected

def test_left_join_two():
    H1 = {'car': "1", 'table': "2"}
    H2 = {'car': 1, 'C': 2}
    actual = left_join(H1 , H2)
    expected = {'car': ["1",1], 'table': ["2","null"]}
    assert actual == expected

def test_left_join_three():
    H1 = {}
    H2 = {}
    actual = left_join(H1 , H2)
    expected = {}
    assert actual == expected

def test_left_join_four():
    H1 = {'salah': "1", 'anas': "2"}
    H2 = {}
    actual = left_join(H1 , H2)
    expected = {'salah': ["1","null"], 'anas': ["2","null"]}
    assert actual == expected

def test_left_join_five():
    H1 = {'test5': "1", 'answer5': "2"}
    H2 = {'test5': 9, 'answer5': 9}
    actual = left_join(H1 , H2)
    expected = {'test5': ["1",9], 'answer5': ["2",9]}
    assert actual == expected