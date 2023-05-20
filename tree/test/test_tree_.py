import pytest
from tree.trees import BinaryTree , BST


def test_1():
    binTree= BinaryTree()
    actual = binTree.pre_order(binTree.root)
    excepted = []
    assert actual == excepted
    
def test_2():
    bst=BST()
    bst.add(bst.root,5)
    bst.add(bst.root,15)    
    bst.add(bst.root,10)    
    actual = bst.in_order(bst.root)
    excepted = [5,10,15]
    assert actual == excepted    
    
def test_3():
    bst=BST()
    bst.add(bst.root,50)
    bst.add(bst.root,40)
    bst.add(bst.root,60)
    
    actual = bst.in_order(bst.root)
    excepted = [40,50,60]
    assert actual == excepted    
    
def test_4(aaa):
    actual = aaa.pre_order(aaa.root) 
    expected = [5,3,2,4,7,6,8]
    assert actual == expected


def test_5(aaa):
    actual = aaa.in_order(aaa.root) 
    expected = [2,3,4,5,6,7,8]
    assert actual == expected

def test_6(aaa):
    actual = aaa.post_order(aaa.root) 
    expected = [2,4,3,6,8,7,5]    
    assert actual == expected


def test_7(aaa):
    actual = aaa.contains(8,aaa.root) 
    expected = True
    assert actual == expected

def test_8(aaa):
    actual= aaa.contains(9,aaa.root) 
    expected = False    
    assert actual == expected

@pytest.fixture
def aaa():
    aaa= BST()
    aaa.add(aaa.root, 5)
    aaa.add(aaa.root, 3)
    aaa.add(aaa.root, 2)
    aaa.add(aaa.root, 4)
    aaa.add(aaa.root, 7)
    aaa.add(aaa.root, 6)
    aaa.add(aaa.root, 8)
    return aaa