# import pytest
# from tree.trees import BinaryTree
# from tree.node import Node
# from tree_intersection.tree_intersection import tree_intersection



# def test_tree_intersection():
#     tree1 = BinaryTree()
#     tree1.root = Node(1)
#     tree1.root.left = Node(2)
#     tree1.root.right = Node(3)
#     tree1.root.left.left = Node(4)
#     tree1.root.left.right = Node(5)
#     tree1.root.right.left = Node(6)
#     tree1.root.right.right = Node(7)

#     tree2 = BinaryTree()
#     tree2.root = Node(1)
#     tree2.root.left = Node(2)
#     tree2.root.right = Node(3)
#     tree2.root.left.left = Node(4)
#     tree2.root.left.right = Node(5)
#     tree2.root.right.left = Node(6)
#     tree2.root.right.right = Node(7)
    

#     assert tree_intersection(tree1.root, tree2.root) == {1, 2, 3, 4, 5, 6, 7}

#     tree2.root.right.right = Node(8)
#     assert tree_intersection(tree1.root, tree2.root) == {1, 2, 3, 4, 5, 6}

#     tree2.root = None
#     assert tree_intersection(tree1.root, tree2.root) == set()