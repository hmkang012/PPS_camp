# B035 동전0

n, k = map(int, input().strip().split())

# 동전 가치 입력받기
arr = [int(input().strip()) for _ in range(n)]

# 동전 리스트를 큰 값부터 작은 값 순으로 정렬
arr.reverse()

min_coins = 0

# 동전 개수 계산
for coin in arr:
    if k == 0:
        break
    if coin <= k:
        min_coins += k // coin
        k %= coin

print(min_coins)
