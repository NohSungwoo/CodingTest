def solution(num_list):
    odd = 0
    enum = 0
    for i in range(len(num_list)) :
        if i % 2 == 0 :
            odd += num_list[i] 
        else :
            enum += num_list[i]
        
    if odd > enum :
        return odd
    else :
        return enum