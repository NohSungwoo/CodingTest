def solution(numbers):
    # 음수와 정수가 섞여 있는 배열이 주어진다.
    # 두 수를 곱해서 가장 큰 경우의 수를 구해라.
    numbers.sort()
    numbers = [numbers[0] * numbers[1],  numbers[-1] * numbers[-2]]
    
    
    return max(numbers)
        