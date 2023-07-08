# Code Challenge 32

---

## tree_intersection method
        
## takes two binary trees and returns the intersection values between them.
## arguments: two binary trees
## returns: list of intersection values

---



---

## Approach & Efficiency

---

## tree_intersection method
## O(n) Time performance --> bbecause we depend on the input size in the loops we use. 
## O(n) Space performance --> the size of memory taken depends on the input size.

---

## Solution:

def tree_intersection(b1,b2):
    i = set()
    hash_table = HashTable()
       
    for a in b1:
        hash_table.set(a,None)
               
    for a in b2:
        if hash_table.has(a):
            
            i.add(a)
            
    
    return i  
       