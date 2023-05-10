# Animal shelter Queue

> - create an animal shelter class as a queue

## Whiteboard Process

![animal shulter](./assest/animal%20shulter.png) 

## Approach & Efficiency

> - Time --> O(1)
> - space -->O(n)

## Solution


class AnimalShelter ():
  
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()

    def enqueue(self,animal):
        if animal["species"] == "dog":
            self.dog.enqueue(animal)
        elif animal["species"] == "cat":
            self.cat.enqueue(animal)

    def dequeue(self,pref):
        if pref is not "dog" or pref is not "cat" :
            return None        
        elif pref == "dog" :
            return  self.dog.dequeue()
        elif pref == "cat" :
            return  self.cat.dequeue()