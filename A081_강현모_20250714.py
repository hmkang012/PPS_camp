T = int(input())

for _ in range(T):
    num = list(map(int, input().split(' ')))[:10]
    num.sort(reverse=True)
    print (num[2])