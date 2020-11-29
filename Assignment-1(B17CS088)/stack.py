class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def top(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
        
     def display(self):
        return self.items

s=Stack()
print(s.isEmpty())
s.push('hai')
s.push(10)
s.push(4.5)
print(s.display())
print(s.size())
print(s.top())
print(s.pop())
print(s.isEmpty())
print(s.top())