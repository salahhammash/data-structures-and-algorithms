class HashTable:
    def __init__(self,size=5):
        self.size = size
        self.map = [None]*size
        
        
    def custom_hash(self, key):
        '''
        takes a key and returns the hashed value of the key as the index
        Args:key
        returns the index 
        '''
        sum_of_asccii = 0
        for ch in key:
            asccii_of_ch = ord(ch)
            sum_of_asccii += asccii_of_ch
        temp = sum_of_asccii*599
        indx = temp%self.size
        return indx      
     
    def set (self,key,val):
        """
        takes a key and a value and adds the key value pair to the hash table
        args:key , value
        returns nothing
        """
        hashed_key = self.custom_hash(key)
        if self.map[hashed_key] is None:
            self.map[hashed_key]=[]
        self.map[hashed_key].append([key,val])    

    def get(self,key):
        """
        takes a key and returns the value associated with the key
        args: key
        returns the value associated with the key
        """
        hashed_key = self.custom_hash(key)
        if self.has(key):
            if len(self.map[hashed_key])==1:
                return self.map[hashed_key][0][1]
            else:
                for i in self.map[hashed_key]:
                    if i[0] == key :
                        return i[1]
        else:
            return "KEY NOT FOUND"            

    def has(self,key):
        """
        takes a key and returns True if the key exists in the hash table and False otherwise
        args: key
        returns True or False
        """
        keys = self.keys()
        if key in keys :
            return True
        return False
    
    def keys (self):
        """
        takes no arguments and returns a list of keys in the hash table
        args: none
        returns a list of keys
        """
        keys_coll = []
        for i in self.map :
            if i is not None :
                for x in i :
                    keys_coll.append(x[0])
        return keys_coll            

# x = HashTable()
# x.set('x',70)
# x.set('a',20)
# # x.set('s',30)
# # x.set('d',40)
# # x.set('r',50)
# # print(x.hash)
# print(x.has('a'))