# 1. 3개의 수를 입력 받기
# - 한 줄로 입력 받기 때문에 list에 저장해서 split하기

# 2. 3개의 수가 같은 경우 상금 계산
# - 10000 + (눈)*1000

# 3. 같은 눈이 2개인 경우 상금 계산
# - 1000 + (같은 눈) *100

# 4. 모두 다른 눈이 나오는 경우
# - (가장 큰 눈) * 100
# - list에서 max값 구하기

n = list(map(int, input().split()))
money = 0

for _ in range(3):
    if n[0] == n[1] == n[2]:
        money = 10000 + n[0] *1000
    elif n[0] == n[1] or n[0] == n[2]:
        money = 1000 + n[0]*100
    elif n[1] == n[2]:
        money == 1000 + n[1]*100
    elif n[0] != n[1] and n[0] != n[2] and n[1] != n[2]:
        max_num = max(n)
        money = max_num * 100

print (money)