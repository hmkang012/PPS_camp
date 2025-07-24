# C029 손익분기점

A, B, C = map(int, input().split())

if B >= C:
    print(-1)
else:
    print (int(A/(C-B)+1))

# -----------------------------------
# 1. A,B,C 값은 한 줄에 있기 때문에 map(int, input().split()) 이렇게 입력을 받고
# 2. A + B == C*x 되는 부분을 구하고, 그 x+1이 답이 된다.
# 3. 손익분기점이 존재하지 않는 경우는 -1을 출력