class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        if len(self.items)>0:
          return self.items.pop()
        return ("No elements in Queue!")


    def size(self):
        return len(self.items)

    def display(self):
        return self.items

q=Queue()
print(q.isEmpty())
q.enqueue('hello')
q.enqueue(88)
q.enqueue(6.72)
print(q.display())
print(q.size())
print(q.dequeue())
print(q.isEmpty())
