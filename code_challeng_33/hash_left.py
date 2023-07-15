def left_join(H1, H2):
    """
    takes two hashmaps and left join them together in the first object
    The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
    The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.    
    
    arguments: two hashmaps
    returns: the first hashmap but left joined with the second hashmap
    """
           
    for key in H1:
        
        if key in H2:
        # it updates the value in H1 by creating a list with two elements
        
            H1[key] = [H1[key] , H2[key]]
        else:
            H1[key] = [H1[key], "null"]
        
    return H1


# i will chaek if the key(name of key) of h1 is inside the key of h2 :
# if true then i will take the key of h1 and create an instence of it with a list and put inside it -->  key[h1] and the values of h1 an h2 
# but if the key of h1  is not inside the key of h2 then create an instence of h1[key]& return for me  --> the value of h1 & null that represent nothing inside h2

if __name__ == "__main__":
    
    H1 = {
        "color": "red",
        #   "age" : "27",
        #   "name1": "salah",
          
        #   "name2": "salah2",
          
        "mustafa" :"aaaa",
        
        
        #   "aaaa":"dddd",
        #   'car': "1"
          }
    
    H2 = {
        "color": "blue",
        #   "age" : "29",
        #   "name2": "salah3",
        #   "cccc":"fff",
        #   'car': 1
        "mustafa1" :"bbbb",
        
          
          
          }
    print(left_join(H1, H2))