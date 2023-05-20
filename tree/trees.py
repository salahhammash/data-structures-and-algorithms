from tree.node import Node

class BinaryTree :
    """This Class creeate a tree where you can add nodes as leaf to it using root.left and root.right
    also there is three fuction that can help you put the values in order, pre order and post order
    
    """
    
    def __init__(self):
        self.root = None

    def pre_order(self,root,list1 = None):
        if list1 == None :
            list1 = []
        if self.root is None :
            return []
        if root is not None:
            list1.append(root.value) 
        # if root.left is not None:
            self.pre_order(root.left,list1)
        # if root.right is not None:
            self.pre_order(root.right,list1)
        return list1   
      
                  

    def in_order(self,root,list2=None):
        if list2 == None :
            list2 = []
        
        if root.left is not None:
           self.in_order(root.left,list2)    
        if root is not None:
            list2.append((root.value)) 
        if root.right is not None:
            self.in_order(root.right,list2)   
        return list2
    
    def post_order(self,root,list3=None):
        if list3 == None :
            list3 = []
        if root.left is not None:
            self.post_order(root.left,list3)    
        if root.right is not None:
            self.post_order(root.right,list3)        
        if root is not None:
            list3.append(root.value) 
        return list3     



class BST(BinaryTree):
    """
     this class is an extend from the binary tree class where it has two fuctions to one to add nodes to the tree dinamicly while keeping it binary 
     and the other is to find if the value exeist in the tree or not 
     """
    def __init__(self):
        self.root = None

    def add(self, root, value):
        if root is None:
            self.root = Node(value)
        else:
            if root.value < value:
                if root.right is None:
                    root.right = Node(value)
                else:
                    self.add(root.right, value)
            else:
                if root.left is None:
                    root.left = Node(value)
                else:
                    self.add(root.left, value)

    def contains(self, value, nodes):
        if nodes is None:
            return False
        elif nodes.value == value:
            return True
        elif nodes.value > value:
            return self.contains(value, nodes.left)
        else:
            return self.contains(value, nodes.right)


        #    

a = BST()
# # a is inctance ( it has evry thing that inside BST )
a.add(a.root,95)
a.add(a.root,10)
a.add(a.root,30)
a.add(a.root,25)
a.add(a.root,40)
a.add(a.root,63)
print(a.contains(1,a.root))
print(a.contains(10,a.root))


print(a.pre_order(a.root))
print(a.in_order(a.root))
print(a.post_order(a.root))

print(a.contains(600,a.root))

