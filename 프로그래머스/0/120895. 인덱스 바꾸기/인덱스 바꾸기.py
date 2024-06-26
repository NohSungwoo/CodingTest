def solution(my_string, num1, num2):
    list_string = list(my_string)
    
    list_string[num1], list_string[num2] = list_string[num2], list_string[num1]
    
    return ''.join(list_string)
    
    