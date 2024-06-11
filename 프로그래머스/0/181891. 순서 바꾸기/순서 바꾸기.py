def solution(num_list, n):
    answer = num_list[n:]
    for i in num_list[:n] :
        answer.append(i)
    
    return answer