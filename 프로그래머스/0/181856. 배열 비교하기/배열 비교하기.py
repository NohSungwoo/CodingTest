def solution(arr1, arr2):
    answer = 0
    arr1_total = 0
    arr2_total = 0
    
    if len(arr1) > len(arr2) :
        return 1
    elif len(arr1) < len(arr2) :
        return -1
    else : 
        for a, b in zip(arr1, arr2) :
            arr1_total += a
            arr2_total += b
    
    if arr1_total > arr2_total :
        return 1
    elif arr1_total < arr2_total :
        return -1
    else :
        return 0