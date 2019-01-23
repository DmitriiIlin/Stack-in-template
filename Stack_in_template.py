
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
    if string_len % 2 != 0:
        output="False"
    else:
        while index<string_len:
            if S[index]=="(":
                a.push(S[index])
            elif S[index]==")" and a.size()>0:
                a.pop()
            else:
                output="False"
            index+=1 
    return output

# Далее приводиться реализация Постфиксной записи выражения. 
math_operations=["+","*","/","-",]
math_digits=[1,2,3,4,5,6,7,8,9,0]
ignore_operation=["(",")"]
result_operations=["="]

def add_element_in_input_list(input_list,a):
    input_list.append(a)
    return input_list

def fitst_Stack_init(input_list):
    input_list_len=len(input_list)
    first_Stack_Lifo=Stack()
    for i in range(input_list_len):
        first_Stack_Lifo.push(input_list[i])
    return first_Stack_Lifo

def operation_logic(first_Stack_Lifo,input_list):
    second_Stack_Lifo=Stack()
    len_first_Stack_lifo=len(input_list)
    for i in range(len_first_Stack_lifo):
        if first_Stack_Lifo.peek() in math_digits:
            second_Stack_Lifo.push(first_Stack_Lifo.peek())
            first_Stack_Lifo.pop()
        elif first_Stack_Lifo.peek() in math_operations:
            A=second_Stack_Lifo.pop()
            B=second_Stack_Lifo.pop()
            if first_Stack_Lifo.peek() == "+":
                second_Stack_Lifo.push(A+B)
            elif first_Stack_Lifo.peek() == "-":
                second_Stack_Lifo.push(A-B)
            elif first_Stack_Lifo.peek() == "/":
                second_Stack_Lifo.push(A/B)
            elif first_Stack_Lifo.peek() == "*":
                second_Stack_Lifo.push(A*B)    
            first_Stack_Lifo.pop()
        elif first_Stack_Lifo.peek() in result_operations:
            print(second_Stack_Lifo.peek())
    return second_Stack_Lifo           

#Z=[]
#add_element_in_input_list(Z,8)
#add_element_in_input_list(Z,2)
#add_element_in_input_list(Z,'+')
#add_element_in_input_list(Z,5)
#add_element_in_input_list(Z,'*')
#add_element_in_input_list(Z,9)
#add_element_in_input_list(Z,'+')
#print(Z)
#j=fitst_Stack_init(Z)
#f=operation_logic(j,Z)
#print(f.peek())

