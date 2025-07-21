# 단어 입력
word = input().strip()

# 모든 문자를 대문자로 변환
word = word.upper()

# 알파벳 빈도수를 저장할 딕셔너리
frequency = {}

# 각 알파벳의 빈도 계산
for char in word:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

# 가장 많이 사용된 알파벳의 빈도 찾기
max_count = max(frequency.values())

# 가장 많이 사용된 알파벳 찾기
most_common = [char for char, count in frequency.items() if count == max_count]

if len(most_common) > 1:
    print('?')
else:
    print(most_common[0])
