# 명함 지갑 만들기
# sizes = 가로 * 세로
# 명함 회전이 가능할 때 최소길이의 지갑 크기는?

def solution(sizes):
    width = []
    height = []
    
    for i in range(len(sizes)):
        sizes[i].sort()
        width.append(sizes[i][0])
        height.append(sizes[i][1])
        
    return max(height) * max(width)