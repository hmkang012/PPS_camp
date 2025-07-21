# A125

N = int(input())
w_list = []
max_weight = 0

for _ in range(N):
    w_list.append(int(input()))

w_list.sort(reverse=True) # 내림차순 정렬

for i in range(N):
    weight = w_list[i] * (i+1)
    if weight > max_weight:
        max_weight = weight
    
print(max_weight)