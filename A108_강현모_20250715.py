N = int(input())

for _ in range(N):
    num = input()
    rev_num = int(num[::-1])

    sum_num = "".join(str(rev_num + int(num)))

    if sum_num == sum_num[::-1]:
        print("YES")
    else:
        print("NO")