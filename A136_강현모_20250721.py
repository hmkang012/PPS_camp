import sys

input = sys.stdin.read
data = input().strip().split('\n')

# 문서와 찾으려는 단어
document = data[0]
word = data[1]

word_length = len(word)
document_length = len(document)

count = 0
start = 0

# 문서에서 단어를 검색
while start <= document_length - word_length:
    # 단어가 문서의 현재 위치에서 시작하는지 확인
    if document[start:start + word_length] == word:
        count += 1
        # 단어가 끝난 위치 이후부터 검색을 계속
        start += word_length
    else:
        start += 1

# 결과 출력
print(count)

