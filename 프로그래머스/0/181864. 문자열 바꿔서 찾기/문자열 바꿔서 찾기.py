def solution(myString, pat):
    answer = 0
    new_string = ''
    
    for i in myString :
        if i == 'A' :
            i = 'B'
            new_string += i
        else : 
            i = 'A'
            new_string += i
    
    if pat in new_string :
        answer = 1
    return answer