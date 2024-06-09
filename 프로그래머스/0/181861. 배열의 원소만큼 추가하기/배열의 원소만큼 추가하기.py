def solution(arr):
    answer = []
     
    for i in arr :
        count = 0    
        while i > count :
            answer.append(i)  
            count += 1
    
    return answer