# stack_queue_pseudo 

## enqueue
Arguments: value
Inserts a value into the PseudoQueue, using a first-in, first-out approach.
## dequeue
Arguments: none
Extracts a value from the PseudoQueue, using a first-in, first-out approach.

## Approach & Efficiency
big(o)
> - Time --> O(n) 
> - space -->O(n)
## Efficiency:
The time complexity of enqueue operation is O(1) because it simply pushes the element onto the inbox stack.
The space complexity is O(n) where n is the number of elements in the queue because it uses two stacks to store the elements.






## Whiteboard Process links
![stack-queue-pseudo](./assest/from%20queue%20to%20stack.png)


### solution 

from code_challeng_stack_and_Queue.stack import Stack

class PseudoQueue:
    """
    this queue is using two stack to implement it self and add to the queue and de queue from it  
    """
    def __init__(self):
        # creating 2 stack instances from stack
       self.stack1 = Stack()
       self.stack2 = Stack()

    def enqueue(self,value):
         #insert a value into class 
         self.stack1.push(value)

    def dequeue(self,value):
        if self.stack1.is_empty() and self.stack2.is_empty():
            return "Queue is empty"
        
        elif self.stack2.is_empty() == False:
            return self.stack2.pop()
        
        elif self.stack1.is_empty() == False and self.stack2.is_empty() == True :
            a = self.stack1.get_size()
            #get_size to know the length
            for i in range(a):
                # rang --> لعمل لووب على قد حجم الستاك 
                b = self.stack1.pop()
                self.stack2.push(b)

            return self.stack2.pop()
        
        
       

            
