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

    def dequeue(self):
        if self.stack1.is_empty() and self.stack2.is_empty():
            return "Queue is empty"
        
        elif self.stack2.is_empty() == False:
            return self.stack2.pop()
        
        elif self.stack1.is_empty() == False and self.stack2.is_empty() == True :
            a = self.stack1.get_size()
            #get_size to know the length to do loop throw it 
            for i in range(a):
                # rang -->  لعمل لووب على قد حجم الستاك 
                # نفس مبدأ عمل لعبة الرول دايسز بدي يجيبلي  6 ارقام مثلا بحددلو عددهم و بس هون حددتلو انه عددهم a 
                b = self.stack1.pop()
                self.stack2.push(b)

            return self.stack2.pop()
        
        
     


            

