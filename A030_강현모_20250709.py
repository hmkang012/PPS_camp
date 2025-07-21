n, current_mood = map(int, input().split())
p_good_to_good, p_good_to_bad, p_bad_to_good, p_bad_to_bad = map(float, input().split())

# 초기 확률 설정
if current_mood == 0:
    good_prob = 1.0
    bad_prob = 0.0
else:
    good_prob = 0.0
    bad_prob = 1.0

# N일 동안의 확률 계산
for _ in range(n):
    next_good_prob = good_prob * p_good_to_good + bad_prob * p_bad_to_good
    next_bad_prob = good_prob * p_good_to_bad + bad_prob * p_bad_to_bad
    good_prob = next_good_prob
    bad_prob = next_bad_prob


print(f"{int(good_prob * 1000):d}")
print(f"{int(bad_prob * 1000):d}")