import sys
input = sys.stdin.read

data = input().split()

N = int(data[0])

# 단어 카운트
group_word_count = 0

# 각 단어 확인
for i in range(1, N + 1):
    word = data[i]
    is_group_word = True
    seen = set()
    last_char = ''
    
    for char in word:
        if char != last_char:
            if char in seen:
                is_group_word = False
                break
            seen.add(char)
            last_char = char
    
    if is_group_word:
        group_word_count += 1

print(group_word_count)
