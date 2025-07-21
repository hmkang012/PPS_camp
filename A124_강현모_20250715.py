# A124 소인수분해 (백준)

N = int(input())
i = 2

while N > 1:
    

    if N % i == 0: # 2로 나누어 떨어진다면
        N = N//i # i로 나누어서 
        print(i) # print i!!
    else:
        i += 1 # 2로 나누어떨어지지 않는다면 i가 3이 될 수 있도록

if N == 1:
        print ()