import sys
input = sys.stdin.read

# 알파벳-숫자 맵핑
dial = {
    'A': 2, 'B': 2, 'C': 2,
    'D': 3, 'E': 3, 'F': 3,
    'G': 4, 'H': 4, 'I': 4,
    'J': 5, 'K': 5, 'L': 5,
    'M': 6, 'N': 6, 'O': 6,
    'P': 7, 'Q': 7, 'R': 7, 'S': 7,
    'T': 8, 'U': 8, 'V': 8,
    'W': 9, 'X': 9, 'Y': 9, 'Z': 9
}

# 입력을 읽고 단어 가져오기
word = input().strip()

# 총 시간 계산
total_time = 0
for char in word:
    total_time += dial[char] + 1

print(total_time)
