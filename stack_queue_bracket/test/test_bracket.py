import pytest

from stack_queue_bracket.stack_queue_brackets import validate_brackets

def test_1 ():
    assert validate_brackets("[[{}]]") == True


def test_2 ():
    assert validate_brackets("[[{}]") == False


def test_3 ():
    assert validate_brackets("[[{abcd}]]") == True

def test_4 ():
    assert validate_brackets("[[{())()()}]]())())(){{{()()}}}") == False

def test_5 ():
    assert validate_brackets("[[{{((0)}}]]") == False    

def test_6 ():
    assert validate_brackets("[[}}]]") == False        

def test_7 ():
    assert validate_brackets("[([") == False        