import pytest
from animal_shelter.stack_queue_animal_shelter import AnimalShelter

def test_1 (a):
    assert a.dequeue("cat") == {"species" : "cat" , "name": "cat1"}

def test_2 (a):
    assert a.dequeue("dog") == {"species" : "dog" , "name": "dog1"}

def test_3():
    b = AnimalShelter()
    assert b.dequeue("camel") == None


@pytest.fixture
def a():
    a = AnimalShelter()
    a.enqueue({"species" : "cat" , "name": "cat1"})
    a.enqueue({"species" : "cat" , "name": "cat2"})
    a.enqueue({"species" : "cat" , "name": "cat3"})
    a.enqueue({"species" : "dog" , "name": "dog1"})
    a.enqueue({"species" : "dog" , "name": "dog2"})
    a.enqueue({"species" : "dog" , "name": "dog3"})
    
    a.dequeue({"species" : "dog" , "name": "dog3"})
    
    return a   
