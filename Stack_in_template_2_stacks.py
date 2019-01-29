
class Stack:
#Реализация класса Стек
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop(-1)

    def push(self, value):
        if len(self.stack)>0:
            #print("insert")
            return self.stack.insert(0,value)
        else:
            #print("append")
            return self.stack.append(value)

    def peek(self):
        if len(self.stack) <= 0:
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)


def check_brackets(S):
    #Функция определяет кол-во символов типа ( или ) и проверяет рав-во кол-ва этих элементов
    string_len=len(S)
    output="True"
    index=0
    a=Stack()
    if S[0]==')':
        output="False"
    if string_len % 2 != 0:
        output="False"
    else:
        while index<string_len and output=="True":
            if S[index]=="(":
                a.push(S[index])
            else:
                if a.size()==0:
                    output="False"
                else:    
                    a.pop()
            index+=1
        if output=="True" and a.size()==0:
            output="True"
        else:
            output="False" 
    return output


S="(())()"
print(check_brackets(S))
