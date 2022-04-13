class Queue:
    def __init__(self):
        self.queue = []
    def enque(self,item):
        self.queue.append(item)
    def deque(self):
        return self.queue.pop(0)
    def top(self):
        return self.queue[len(self.queue)-1]
    def return_queue(self):
        return self.queue
q=Queue()
q.enque(1)
q.enque(2)
q.enque(3)
q.enque(4)
print(f"Queue: {q.return_queue()}")
print(f"Top: {q.top()}")
q.deque()

print(f"Queue: {q.return_queue()}")
print(f"Top: {q.top()}")