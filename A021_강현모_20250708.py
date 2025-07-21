import sys

input = sys.stdin.readline

N = int(input())  # 플러그의 개수
total = 0

for _ in range(N):
    total += int(input().strip()) # 각 줄마다 input하기 위해 strip 사용

result = total - (N - 1)
print(result)