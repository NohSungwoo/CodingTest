def solution(s):
    list_s = list(map(int, s.split()))
    answer = f'{min(list_s)} {max(list_s)}'
    return answer