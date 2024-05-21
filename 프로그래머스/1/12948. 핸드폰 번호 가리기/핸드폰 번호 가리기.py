def solution(phone_number) :
    answer_b = '*' * (len(phone_number)-4)
    answer = ''.join(reversed(phone_number[:-5:-1]))
    return answer_b + answer