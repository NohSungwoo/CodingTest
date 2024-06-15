def solution(num, k):
    count = 1
    
    for i in str(num) :
        if i == str(k) :
            return count
        count += 1
    return -1