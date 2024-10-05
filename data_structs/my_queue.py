# FIFO Data Structure
# Front of queue: head; Back of queue: tail
class my_queue:
    def __init__(self) -> None:
        self.queue = []

    def __str__(self) -> str:
        return str(self.queue)

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        self.queue.pop(0)

    def head(self):
        if len(self.queue) == 0:
            return
        else:
            return self.queue[0]
    
    def tail(self):
        if len(self.queue) == 0:
            return
        else:
            return self.queue[-1]
        
    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        return len(self.queue == 0)
    

        
    
# testing

q = my_queue()
q.enqueue("Tom")
q.enqueue("Jerry")
q.enqueue("Bob")
q.enqueue("Bert")
q.enqueue("Ernie")
# print(q)

q.dequeue()
q.dequeue()
print(q.tail())
# print(q)
# print(q.head())
q.dequeue()
print(q)
print(q.head())
q.dequeue()
q.dequeue()
print(q)
print(q.head())