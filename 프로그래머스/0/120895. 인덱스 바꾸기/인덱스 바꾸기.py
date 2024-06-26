def solution(my_string, num1, num2):
    list_string = []
    change_string = ''
    
    for i in my_string:
        list_string += i
    
    list_string[num1], list_string[num2] = list_string[num2], list_string[num1]
    
    for i in list_string:
        change_string += i
    
    return change_string
    
    