import Stack_in_template 

class Stack_LiFo(Stack_in_template.Stack):
    pass

math_operations=["+","*","/","-",]
math_digits=[1,2,3,4,5,6,7,8,9,0]
ignore_operation=["(",")"]
result_operations=["="]

def add_element_in_input_list(input_list,a):
    input_list.append(a)
    return input_list

def fitst_Stack_init(input_list):
    input_list_len=len(input_list)
    first_Stack_Lifo=Stack_LiFo()
    for i in range(input_list_len):
        first_Stack_Lifo.push(input_list[i])
    return first_Stack_Lifo

def operation_logic(first_Stack_Lifo,input_list):
    second_Stack_Lifo=Stack_LiFo()
    len_first_Stack_lifo=len(input_list)
    for i in range(len_first_Stack_lifo):
        if first_Stack_Lifo.peak() in math_digits:
            second_Stack_Lifo.push(first_Stack_Lifo.peak())
            first_Stack_Lifo.pop()
        elif first_Stack_Lifo.peak() in math_operations:
            A=second_Stack_Lifo.pop()
            B=second_Stack_Lifo.pop()
            if first_Stack_Lifo.peak() == "+":
                second_Stack_Lifo.push(A+B)
            elif first_Stack_Lifo.peak() == "-":
                second_Stack_Lifo.push(A-B)
            elif first_Stack_Lifo.peak() == "/":
                second_Stack_Lifo.push(A/B)
            elif first_Stack_Lifo.peak() == "*":
                second_Stack_Lifo.push(A*B)    
            first_Stack_Lifo.pop()
        elif first_Stack_Lifo.peak() in result_operations:
            print(second_Stack_Lifo.peak())
    return second_Stack_Lifo           

Z=[]
add_element_in_input_list(Z,8)
add_element_in_input_list(Z,2)
add_element_in_input_list(Z,'+')
add_element_in_input_list(Z,5)
add_element_in_input_list(Z,'*')
add_element_in_input_list(Z,9)
add_element_in_input_list(Z,'+')
print(Z)
j=fitst_Stack_init(Z)
f=operation_logic(j,Z)
print(f.peak())
