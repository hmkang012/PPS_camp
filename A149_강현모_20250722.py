# A149 덩치

import sys
input = sys.stdin.read

data = input().strip().split('\n')

num = int(data[0])

# 각 사람의 키와 몸무게 받기
dimensions = [tuple(map(int, line.split())) for line in data[1:num + 1]]

grades = [] # 결과를 저장~

# 각 사람에 대해 등수를 계산
for i in range(num):
    grade = 1
    for j in range(num):
        if dimensions[i][0] < dimensions[j][0] and dimensions[i][1] < dimensions[j][1]:
            grade += 1
    grades.append(grade)

print(' '.join(map(str, grades)))