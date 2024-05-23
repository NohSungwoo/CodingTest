def solution(left, right):
    answer = 0
    num_list = list(range(left, right + 1))
    for i in num_list :
        count = 0
        for x in range(1, i + 1) :
            if i % x == 0 :
                count += 1
        if count % 2 == 0:
            answer += i
        else :
            answer -= i
    return answer