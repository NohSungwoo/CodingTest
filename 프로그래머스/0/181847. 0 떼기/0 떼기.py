def solution(n_str):
    count = 0
    for i in n_str :
        if int(i) > 0 :
            break
        count += 1
    return n_str[count:]