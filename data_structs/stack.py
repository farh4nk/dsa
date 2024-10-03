# LIFO Data Structure
# Positions are numbered from 1 at the top of the stack and increase towards the bottom

class Stack:
    def __init__(self) -> None:
        self.stack = []

    def __str__(self) -> str:
        result = ''
        pos = 1
        for el in self.stack[::-1]:
            
            result += f"{pos}: -- {el} --\n"
            pos += 1
        return result

    def length(self):
        return len(self.stack)
    
    def empty(self):
        return len(self.stack) == 0
    
    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop(-1)
    
    def peek(self):
        return self.stack[-1]
    
    # return position of element if found, otherwise returns error msg
    def search(self, element):
        if element in self.stack:
            return self.stack[::-1].index(element) + 1
        else:
            return f"The stack doesn't contain the element {element}"
        
# testing
s = Stack()
# print(s.length())
s.push(1)
# s.push("apple")
# print(s)
# print(s.pop())
s.push("orange")
s.push(5)
print(s)
print(f"the element 5 is at the posiiton {s.search(5)}")
print(s.search(6))
