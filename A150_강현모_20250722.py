sum = 0
result = 0
result_list = []

N = int(input())

num = list(map(int, input().split(' ')))[:N]

for i in range(1, N):
    num[i] = max(num[i], num[i] + num[i-1])

print (max(num))
