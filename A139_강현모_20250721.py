import sys

input = sys.stdin.read().strip()

S = input

# 블록 카운팅을 위한 초기화
zero_blocks = 0
one_blocks = 0

# 현재 블록 상태
current_char = S[0]
if current_char == '0':
    zero_blocks += 1
else:
    one_blocks += 1

# 문자열을 순회하며 블록 개수 계산
for char in S[1:]:
    if char != current_char:
        if char == '0':
            zero_blocks += 1
        else:
            one_blocks += 1
        current_char = char

# 0으로 변환할 때와 1로 변환할 때의 최소 작업 횟수
result = min(zero_blocks, one_blocks)

print(result)

