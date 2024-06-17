num = int(input())

def solution(num):
    count = 0
    total_num = 0

    for i in range(1, num + 1):
        if num - total_num < i:
            return count
        total_num += i
        count += 1

    return count  

result = solution(num)
print(result)