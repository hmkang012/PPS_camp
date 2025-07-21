num = input()
N, M = map(int, num.split())

count1 = 0
count2 = 0

while N >1:
    N -= 1
    count1 += 1

while M >1:
    M -= 1
    count2 += 1

sum = count1 + count2 + 1
print (sum)