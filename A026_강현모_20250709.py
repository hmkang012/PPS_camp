# 프로그래머스 - 하샤드 수
def solution(x):
    a = []

    for i in str(x):
        a.append(int(i))

    answer = int(x) % (int(sum(a)))

    if answer == 0:
        return True
    elif answer == 1:
        return False

x = input()
print (solution(x))