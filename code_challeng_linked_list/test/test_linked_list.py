import pytest

from code_challeng_linked_list.linked_list import LinkedList

def test_1():
    ll = LinkedList()
    assert str(ll.tostring()) == "Empty LinkeList"

def test_2(AA):
    assert str(AA.tostring()) == "C -> B -> A ->  Null"

def test_3():
    ll = LinkedList()
    ll.insert("A")
    ll.insert("B")
    assert str(ll.tostring()) == "B -> A ->  Null"

def test_4(AA):
    assert AA.includes('A') == True

def test_5(AA):
    assert AA.includes('D') == False

def test_6(AA):
    assert AA.head.value == "C"

def test_7(AA):
    expected = "C -> B -> A -> D ->  Null" 
    AA.append("D")
    actual = str(AA.tostring())       
    assert expected == actual 

def test_8(AA):
    expected = "C -> B -> A -> D -> E ->  Null" 
    AA.append("D")
    AA.append("E")
    actual = str(AA.tostring())       
    assert expected == actual 

def test_9(AA):
    expected = "C -> B -> g -> A ->  Null" 
    AA.insert_before('A','g')
    actual = str(AA.tostring())       
    assert expected == actual 

def test_10(AA):
    expected = "g -> C -> B -> A ->  Null" 
    AA.insert_before('C','g')
    actual = str(AA.tostring())       
    assert expected == actual 

def test_11(AA):
    expected = "C -> B -> f -> A ->  Null" 
    AA.insert_after('B','f')
    actual = str(AA.tostring())       
    assert expected == actual

def test_12(AA):
    expected = "C -> B -> A -> f ->  Null" 
    AA.insert_after('A','f')
    actual = str(AA.tostring())       
    assert expected == actual

def test_13(AA):
    expected= "Error : Your input can't be more than the length" 
    actual = AA.kthFromEnd(4)
    assert  expected == actual  
def test_14(AA):
    expected= "Error : Your input can't be more than the length" 
    actual = AA.kthFromEnd(7)
    assert  expected == actual  

def test_15():
    LL= LinkedList()
    LL.insert("A")
    assert LL.kthFromEnd(0) == "A"

def test_16(AA):
    expected= "C" 
    actual = AA.kthFromEnd(2)
    assert  expected == actual  


def test_17():
    ll=LinkedList()
    ll.append("a")
    ll.append("b")
    ll.append("c") 
    ll2=LinkedList()
    ll2.append("1")
    ll2.append("2")
    ll2.append("3") 
    excepted="a -> 1 -> b -> 2 -> c -> 3 ->  Null"
    actual=LinkedList.tostring(ll.zip_list(ll,ll2))
    assert actual == excepted 
"""
“Happy Path” where the first linked list is shorter
"""
def test_18():
    ll=LinkedList()
    ll.append("a")
    ll.append("b")
    ll2=LinkedList()
    ll2.append("1")
    ll2.append("2")
    ll2.append("3") 
    excepted="a -> 1 -> b -> 2 -> 3 ->  Null"
    actual= LinkedList.tostring(ll.zip_list(ll,ll2))
    assert actual == excepted   
"""
“Happy Path” where the second linked list is shorter
"""
def test_19():
    ll=LinkedList()
    ll.append("a")
    ll.append("b")
    ll.append("c") 
    ll2=LinkedList()
    ll2.append("1")
    ll2.append("2")
    excepted="a -> 1 -> b -> 2 -> c ->  Null"
    actual=LinkedList.tostring(ll.zip_list(ll,ll2))
    assert actual == excepted     
"""
“edge case 1” where the first linked list is empty 
"""
def test_20():
    ll=LinkedList()
    ll.append("a")
    ll.append("b")
    ll.append("c") 
    ll2=LinkedList()
    excepted="a -> b -> c ->  Null"
    actual=LinkedList.tostring(ll.zip_list(ll,ll2))
    assert actual == excepted
"""
“edge case 2” where the second linked list is empty 
"""
def test_21():
    ll=LinkedList() 
    ll2=LinkedList()
    ll2.append("1")
    ll2.append("2")
    excepted="1 -> 2 ->  Null"
    actual=LinkedList.tostring(ll.zip_list(ll,ll2))
    assert actual == excepted   
"""
“edge case 3” where both linked lists are empty
"""
def test_22():
    ll=LinkedList() 
    ll2=LinkedList()
    excepted="Both lists are empty"
    actual=str(ll.zip_list(ll,ll2))
    assert actual == excepted 


@pytest.fixture
def AA():
    AA = LinkedList()
    AA.insert('A')
    AA.insert('B')
    AA.insert('C')
    return AA

@pytest.fixture(autouse=True)
def clean():
    """runs before each test automatically.
    This is necessary because otherwise the count added in one test
    will bleed over to other tests
   
    """

    LinkedList.count = 0

