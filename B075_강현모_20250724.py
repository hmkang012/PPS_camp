import sys

input = sys.stdin.read
N = int(input().strip())

# 동전 종류
coins = [1, 2, 5, 7]

# dp 배열을 정의하고 초기화
dp = [float('inf')] * (N + 1)
dp[0] = 0

# dp 배열 갱신하는..
for i in range(1, N + 1):
    for coin in coins:
        if i >= coin:
            dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[N])