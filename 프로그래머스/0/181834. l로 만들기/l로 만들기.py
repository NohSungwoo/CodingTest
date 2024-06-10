def solution(myString):    
    answer = ''
    
    for char in myString :
        if char < 'l' :
            char = 'l'
        answer += char
    
    return answer