def solution(myString):
    answer = ''
    
    for char in myString.lower() :
        if char == 'a' :
            char = 'A' 
        answer += char
        
    return answer