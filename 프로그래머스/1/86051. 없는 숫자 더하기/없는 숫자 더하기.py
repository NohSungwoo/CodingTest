def solution(numbers):
    list_perfect = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    answer = 0
    for i in numbers :
        position = list_perfect.index(i)
        list_perfect.remove(list_perfect[position])
    answer += sum(list_perfect)
    return answer