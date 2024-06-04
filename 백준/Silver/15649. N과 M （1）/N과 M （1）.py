def generate_sequences(N, M):
    def backtrack(current_sequence):
        if len(current_sequence) == M:
            print(" ".join(map(str, current_sequence)))
            return

        for num in range(1, N + 1):
            if num not in current_sequence:
                current_sequence.append(num)
                backtrack(current_sequence)
                current_sequence.pop()

    backtrack([])

# 입력 받기
N, M = map(int, input().split())

# 수열 생성 및 출력
generate_sequences(N, M)