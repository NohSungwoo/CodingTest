def solution(n, lost, reserve):
    # 모든 학생들이 체육복을 한 벌 가지고 있다고 가정합니다.
    clothes = {i: 1 for i in range(1, n + 1)}
    
    # 도난당한 학생들의 체육복 개수를 줄입니다.
    for l in lost:
        clothes[l] -= 1
    
    # 여벌 체육복을 가진 학생들의 체육복 개수를 늘립니다.
    for r in reserve:
        clothes[r] += 1
    
    # 여벌 체육복을 빌려줄 수 있는지 확인합니다.
    for i in range(1, n + 1):
        if clothes[i] == 0:
            if i - 1 > 0 and clothes[i - 1] == 2:
                clothes[i] += 1
                clothes[i - 1] -= 1
            elif i + 1 <= n and clothes[i + 1] == 2:
                clothes[i] += 1
                clothes[i + 1] -= 1
    
    # 체육복을 한 벌 이상 가진 학생들의 수를 셉니다.
    count = sum(1 for i in range(1, n + 1) if clothes[i] > 0)
    
    return count

# 예시
n = 5
lost = [2, 4]
reserve = [1, 3, 5]
        