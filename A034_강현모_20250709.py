num = []
div_list = [0]*10

for i in range(10):
    num.append(int(input()))

for i in range(10):
    div_list[i] = num[i] % 42

unique_num = set(div_list)
total = len(unique_num)
print (total)