import sys
input = sys.stdin.read
data = input().strip()

M, N = map(int, data.split())

# 숫자를 영어 단어로 변환하기 위해 설정
words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# M 이상 N 이하의 모든 정수를 리스트에 저장
numbers = list(range(M, N + 1))

# 숫자와 그에 해당하는 영어 단어 문자열을 저장
sortable = []

for num in numbers:
    # 숫자를 단어로 변환
    num_as_words = ' '.join(words[int(digit)] for digit in str(num))
    sortable.append((num_as_words, num))

# 사전순으로 정렬
sortable.sort()

# 정렬된 결과에서 숫자만 빼가
sorted_numbers = [num for _, num in sortable]

for i in range(0, len(sorted_numbers), 10):
    print(' '.join(map(str, sorted_numbers[i:i + 10])))