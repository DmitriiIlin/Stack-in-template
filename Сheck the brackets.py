import Stack_in_template

def check_brackets(S):
    #Функция определяет кол-во символов типа ( или ) и проверяет рав-во кол-ва этих элементов
    string_len=len(S)
    output="True"
    index=0
    a=Stack_in_template.Stack()
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

