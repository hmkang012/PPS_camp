# 1. N을 int로 받고
# 2. for문의 범위를 N으로 정해서 그만큼 숫자를 list에 append -> [:N]으로
# 3. v를 입력받고
# 4. list에 v가 몇 개 있는지 count(v)를 해서 print하기

N = int(input())

num_list = list(map(int, input().split()))[:N]

v = int(input())
print (num_list.count(v))