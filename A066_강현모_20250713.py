N = int(input())
num_list = list(map(int, str(N)))

num_list.sort(reverse=True) # 오름차순

for i in num_list:
    print(i, end='')