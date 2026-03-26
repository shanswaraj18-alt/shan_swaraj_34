#class solution():
   # def __init__(self):
    #    self.items=[]
    #def empty(self):
     #   if len(self.items)==0:
      #      print("empty queue")    
    #def enqueue(self,items):
     #   self.items.append(items) 
      #  return self.items
    #def dequeue(self):
     #   x =self.items.pop(0)
      #  return x 
    #def front(self):
     #   if len(self.items)==0:
      #      print("queue is empty")
       # return self.items[0]
    #def rear(self):
     #   if len(self.items)==0:
      #      print("queue is empty")
       # return self.items[-1]    
    #def size(self):
     #   return len(self.items)
#obj = solution()    
#obj.enqueue(45)
#obj.enqueue(46)
#obj.enqueue(98)
#obj.enqueue(65)
#obj.enqueue(18)
#print(obj.dequeue())
#print(obj.front())
#print(obj.rear())

#implementation of stack using queue
from collections import deque
#class solution():
    #def __init__(self):
     #   self.queue=deque()
    #def push(self,items):
     #   self.queue.append(items)
      #  for _ in range(len(self.queue)-1):
       #     self.queue.append(self.queue.popleft())
        #return self.queue
    #def pop(self):
     #   if len(self.queue)==0:
      #      print("stack is empty")
       # return self.queue.popleft()
    #def top(self):
     #    if len(self.queue)==0:
      #      print("stack is empty")
       #  return self.queue[0]   
#stackusingqueue = solution()
#stackusingqueue.push(12)
#stackusingqueue.push(23)
#stackusingqueue.push(45)
#stackusingqueue.push(78)
#print(stackusingqueue.pop())
#print(stackusingqueue.pop())
#print(stackusingqueue.top())

#implement queue using two stack
#class solution():
 #   def __init__(self):
  #      self.st1 = []
   #     self.st2 = []
    #def push(self,x):
     #   while self.st1:
      #      self.st2.append(self.st1.pop())
       # self.st1.append(x)
        #while self.st2:
         #   self.st1.append(self.st2.pop()) 
    #def pop(self):
     #   if len(self.st1)==0:
      #      print("queue is empty")
       # return self.st1.pop()
    #def peek(self):
     #   if len(self.st1)==0:
      #      print("queue is empty")
       # return self.st1[-1]   
#queuusingstack=solution()
#queuusingstack.push(37)
#queuusingstack.push(45)
#queuusingstack.push(63)
#print(queuusingstack.pop())
#print(queuusingstack.peek())

#implimenting stack using dll
print("running")
class node:
    def __init__(self,value):
        self.value=value
        self.prev = None
        self.next=None
class queueusngdll:
    def __init__(self):
        self.head=None
    def enqueu(self,value):
        new_node = node(value)
        if self.head== None:
            self.head=new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next=new_node
        new_node.prev = temp
    def deque(self):
        if self.head is None:
            print("queue is empty")
            return
        if self.head.next ==None:
            self.head = None
            return    
        self.head =self.head.next
        self.head.prev = None
    def peek(self):
        if self.head is None:
            print("queue is empty")
            return None
        return self.head.value
queu = queueusngdll()
queu.enqueu(23)
queu.enqueu(78)
queu.enqueu(24)
queu.deque()
print(queu.peek())        





               



        
    
