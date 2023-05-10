from code_challeng_stack_and_Queue.Queue import Queue

class AnimalShelter ():
    """ this class use two queue to add dogs to one of them and cats to the another and dequeue depands on the pref for the dequeue function
    """
     
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()

    def enqueue(self,animal):
        if animal["species"] == "dog":
            self.dog.enqueue(animal)
        elif animal["species"] == "cat":
            self.cat.enqueue(animal)

    def dequeue(self,pref):
        if pref != "dog" and pref != "cat" :
            return None        
        elif pref == "dog" :
            return  self.dog.dequeue()
        elif pref == "cat" :
            return  self.cat.dequeue()
    
    
