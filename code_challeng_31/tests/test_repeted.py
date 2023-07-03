import pytest

from code_challeng_31.repeted import repeated_word

def test_one():
    actual ="It was a queer, sultry summer, summer summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    expected = "summer"
    assert repeated_word(actual) == expected 


def test_two():
    actual ="It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    expected = "it"
    assert repeated_word(actual) == expected 

def test_three():
    actual ="Once upon a time, there was brave princess who..."
    expected = None
    assert repeated_word(actual) == expected     