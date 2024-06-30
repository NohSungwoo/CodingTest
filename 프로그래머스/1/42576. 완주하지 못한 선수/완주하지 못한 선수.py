def solution(participant, completion):
    hash_map = {}
    
    # 참가자 이름을 해시맵에 추가
    for p in participant:
        if p in hash_map:
            hash_map[p] += 1
        else:
            hash_map[p] = 1
            
    # 완주한 참가자 이름을 해시맵에서 감소
    for c in completion:
        if c in hash_map:
            hash_map[c] -= 1
            
    # 값이 0이 아닌 참가자를 찾음
    for key in hash_map:
        if hash_map[key] != 0:
            return key

# 예시
participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))  # "leo"가 출력됨