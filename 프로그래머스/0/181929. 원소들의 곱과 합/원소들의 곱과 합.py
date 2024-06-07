def solution(num_list):
    multiple_num = 1
    sum_num = 0
    
    for i in num_list :
        multiple_num = multiple_num * i
        sum_num += i
        print(multiple_num)
        
    if sum_num ** 2 > multiple_num :
        return 1
    else : 
        return 0