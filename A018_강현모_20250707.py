import sys

# 입력
input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:N+1]))
B = list(map(int, data[N+1:2*N+1]))

# A는 오름차순으로 정렬, B는 내림차순으로 정렬
A.sort()
B.sort(reverse=True)

# S 계산
S = sum(a * b for a, b in zip(A, B))

print(S)