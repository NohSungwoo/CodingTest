def solution() :
    num = int(input())
    count = 0
    total_num = 0

    for i in range(1, num + 1) :
        total_num += i    
        count += 1

        if num == 1 :
            return 1
        if total_num > num :
            return count - 1

print(solution())