def solution(t, p):
    count = 0
    list_t = []
    
    while count != len(t) - len(p) + 1 :
        list_t.append(t[count : count + len(p)])
        count += 1
        
    count = 0
    
    for i in list_t :
        if int(i) <= int(p) :
            count += 1
    
    return count