import sys
input = sys.stdin.read

data = input().split()
index = 0

T = int(data[index])
index += 1

results = []

for _ in range(T):
    k = int(data[index])
    n = int(data[index + 1])
    index += 2
    
    # 아파트 배열 초기화 (0층부터 k층, 1호부터 n호)
    apt = [[0] * (n + 1) for _ in range(k + 1)]
    
    # 0층 초기화 (1, 2, 3, ..., n)
    for i in range(1, n + 1):
        apt[0][i] = i
    
    # 각 층별 인원 계산
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            apt[i][j] = apt[i][j - 1] + apt[i - 1][j]
    
    # 저장~
    results.append(apt[k][n])

# 출력
for result in results:
    print(result)
