
class Stack:
#Реализация класса Стек
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop(-1)

    def push(self, value):
        print("insert")
        return self.stack.append(value)

    def peek(self):
        if len(self.stack) <= 0:
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)



