def solution(numLog):
    answer = ''
    
    for i, num in zip(range(1, len(numLog)), numLog) :
        if num + 1 ==  numLog[i] :
            answer += 'w'
        elif num - 1 == numLog[i] :
            answer += 's'
        elif num + 10 == numLog[i] :
            answer += 'd'
        else :
            answer += 'a'
        
    return answer