from Hash_table.hashtable import HashTable
# from tree.node import Node



def tree_intersection(b1,b2):
    '''
    find the intersection between 2 binary tree 
    
    arg : b1 ,b2 
    
    return intersection as a set 
    '''
    
    
    i = set()
    #to store the intersection elements
    
    hash_table = HashTable()
    #  This hash table will be used to efficiently store and look up values.
    
    for a in b1:
        hash_table.set(a)
        #This method internally computes the hash value of a and stores it in the hash table.        
        
    for a in b2:
        #the function iterates over each element a in the second binary tree b2 using another for loop.

        if hash_table.has(a):
            #If the hash table contains a, it means that a is present in both b1 and b2.
            i.add(a)
            #If a is found in the hash table, it is added to the intersection set i using the add method
    
    return i  
    # Finally, the function returns the intersection set i.
       
