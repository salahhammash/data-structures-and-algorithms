from code_challeng_stack_and_Queue.Queue import Queue

class AnimalShelter ():
    """ this class use two queue to add dogs to one of them and cats to the another and dequeue depands on the pref for the dequeue function
    """
     
    def __init__(self):
        self.pet = Queue()
        

    def enqueue(self,animal):
        
        self.pet.enqueue(animal)
        
        

    def dequeue(self,pref):             
        if pref != "dog" and pref != "cat" :
            return None       
        
        else :
            a = self.pet.front
            print(a.value["species"])
            while a["species"] != pref:
                a = a.next
                
                if a["species"] == pref:
                    x = a["name"]
                    self.pet.dequeue(a)
                    return x
                

                
aa = AnimalShelter() 
aa.enqueue({"species" : "cat" , "name": "cat1"})     

aa.dequeue("cat")
           
                

    
#  dog -> cat -> none 

