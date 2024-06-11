def solution(s1, s2):
    count = 0
    
    for string in s1 :
        if string in s2 :
            count += 1
    return count