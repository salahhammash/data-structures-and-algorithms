from tree.node import Node
from code_challeng_stack_and_Queue.Queue import Queue

class BinaryTree :
    """This Class creeate a tree where you can add nodes as leaf to it using root.left and root.right
    also there is three fuction that can help you put the values in order, pre order and post order
    
    """
    
    def __init__(self):
        # at first the root will be none (i have a root but without value)
        self.root = None
       

    def pre_order(self,root,list1 = None):
        # tree well return for me a list
        
        # if root dosent have a value => none return empty list  
        if self.root is None :
            return []
        # just to creat a list if i dont have at first time 
        if list1 == None :
            list1 = []
            
        # if the root has a value append(push) the value to the list    
        if root is not None:
            list1.append(root.value) 
        # if root.left is not None:
        # we will call the function back as recurgen
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

    def max_val(self):
    
        max= self.root.value
        
        if self.root is None :
            return "Empty Tree"   
        
        in_ord= self.in_order(self.root)
        for i in range(len(in_ord)):                
            if in_ord[i] > max:
                max = in_ord[i]
                
        return max  
    

    def breadth_first(self,node):
        queue= Queue()
        list_breadth = []
        
        if node is None :
            return []
        else:
            queue.enqueue(node)
        while queue.front:
            node = queue.dequeue()
            list_breadth.append(node.value)
            if node.left :
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)    
        return list_breadth    
        

class BST(BinaryTree):
    """
     this class is an extend from the binary tree class where it has two fuctions to one to add nodes to the tree dinamicly while keeping it binary 
     and the other is to find if the value exeist in the tree or not 
     """
    def __init__(self):
        # first of all root dosent have a value 
        self.root = None
        

    def add(self, root, value):
        #this def to creat a tree from scratch 
        
        # this if staetment will enterd just at first time to take the value that i passed (a.add(a.root,95))
        if root is None:
            self.root = Node(value)
            
        else:
            # here will enterd after the first if staetment when i add secound (or more) number (a.add(a.root,10))
            # root.value => 95 ,,, value => 10 secound num
            if root.value < value:
                if root.right is None:
                    # will search if the rigth is none or not => if yes creat new one and pass the value that i added for it  
                    root.right = Node(value)
                else:
                    # when you want too add a new value after you creat one (Node) --> will do recargen for the new value & make root.right = root
                    self.add(root.right, value)
            else:
                if root.left is None:
                    root.left = Node(value)
                else:
                    self.add(root.left, value)
                    
        
   # loop throw Nodes that inside the tree , then compare evry value with max  , if > max ==> max = value of node 
  
    
 
               
        
        
    def contains(self, value, nodes):
        # to check if the number(nodes) that i passed(give to it) inside the tree or not 
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
# a.add(a.root,5)
# a.add(a.root,3)
# a.add(a.root,2)
# a.add(a.root,4)
# a.add(a.root,7)
# a.add(a.root,6)
# a.add(a.root,8)

# a.add(a.root,-95)
# a.add(a.root,-10)
# a.add(a.root,-30)
# a.add(a.root,-25)
# a.add(a.root,-400)
# a.add(a.root,-63)
# print(a.contains(1,a.root))
# print(a.contains(10,a.root))


# print(a.pre_order(a.root))
# print(a.in_order(a.root))
# print(a.post_order(a.root))
# print(a.max)
# print(a.max_val(a.in_order(a.root)))

# print(a.contains(600,a.root))
# print(a.max_val())
print(a.breadth_first(a.root))





