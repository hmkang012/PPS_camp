score = []

for i in range(8):
    score.append(int(input()))

# 내림차순 정렬
sorted_score = sorted(score, reverse=True)

# 상위 5개의 점수 선택
top5_score = sorted_score[:5]
total = sum(top5_score)

# 상위 5개의 점수가 몇 번째로 입력되었는지 찾기
index_num = {score.index(value) + 1: value for value in top5_score}

# 문제 번호를 오름차순으로 정렬
sorted_indices = sorted(index_num.keys())

print(total)
print(' '.join(map(str, sorted_indices)))
