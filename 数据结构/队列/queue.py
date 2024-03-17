"""
队列的实现方式：环形队列
"""

class Quene:
    def __init__(self, size=100):
        self.quene=[0 for _ in range(100)]
        self.front = 0
        self.rear = 0
        self.size = size

    def push(self, element):
        if not self.is_filled():
            self.rear = (self.rear+1) % self.size
            self.quene[self.rear]=element
        else:
            raise IndexError('Queue is filled.')

    def pop(self):
        if not self.is_empty():
            self.front = (self.front+1) % self.size
            return self.quene[self.front]
        else:
            raise IndexError('Queue is empty.')

    def is_empty(self):
        return self.rear == self.front

    def is_filled(self):
        return (self.rear+1) % self.size == self.front



q = Quene(5)
for i in range(4):
    q.push(i)
print(q.quene)
print(q.pop())