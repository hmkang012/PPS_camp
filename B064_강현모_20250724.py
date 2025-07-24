# B064 두 수의 합

n = int(input())
n_list = list(map(int, input().split()))
x = int(input())

count = 0
num_set = set(n_list)  # set으로 n_list를 바꾸기 (시간 단축을 위함)

for i in n_list:
    target = x - i
    if target in num_set:
        if i != target:  # i와 target이 같지 않을 때
            count += 1
            num_set.remove(i)
            num_set.remove(target)
        else:  # i와 target이 같을 때 (중복 제거를 위해)
            if n_list.count(i) > 1:
                count += 1
                num_set.remove(i)

print(count)


# -----------------------------------
# 1. n개의 원소들을 list로 받고
# 2. for문을 통해서 list를 돌면서,,
# 2-2. list[0]의 값과 그 다음값(i+1)들이 x가 되는지 확인하고 (중복을 제거해야 함)
# 3. x가 되는 값들이 있으면 count += 1
# 4. 마지막으로는 count를 출력