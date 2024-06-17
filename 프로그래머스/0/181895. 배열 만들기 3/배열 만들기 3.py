def solution(arr, intervals):
    tem = []   
    answer = []
    tem.append(arr[intervals[0][0] : intervals[0][1] + 1])
    tem.append(arr[intervals[1][0] : intervals[1][1] + 1])
    
    [answer.append(num) for num_list in tem for num in num_list]
    
    return answer