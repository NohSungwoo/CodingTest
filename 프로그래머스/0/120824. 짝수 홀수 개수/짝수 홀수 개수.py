def solution(num_list):
    answer = []
    count_1 = 0
    count_2 = 0
    
    for i in num_list :
        if i % 2 == 0 :
            count_2 += 1
        else : 
            count_1 += 1
    answer.append(count_2)
    answer.append(count_1)
    
    return answer