import sys
input=sys.stdin.readline

N = int(input())

num_list = []
count_list = [0] * N

for _ in range(N):
  num_list.append(int(input()))

num_list.sort() # 중앙값을 구하기 위함

# 산술평균 구하기
total = 0
total = sum(num_list)
mean = round(total/N)
print (mean)

# 중앙값
print (num_list[len(num_list)//2])

# 최빈값
dict = {}
for i in num_list:
  if i not in dict:
    dict[i] = 1
  else:
    dict[i] += 1

max_cnt = max(dict.values())
max_arr = sorted([k for k,v in dict.items() if v == max_cnt])

if len(max_arr)>1:
  print(max_arr[1])
else:
  print(max_arr[0])


# 범위
print (max(num_list)-min(num_list))