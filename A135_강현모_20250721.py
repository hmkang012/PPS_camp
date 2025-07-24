import sys

input = sys.stdin.read
data = input().strip().split('\n')

N = int(data[0])

book_count = {} # 빈도 계산

# 책 제목 입력받고 빈도 계산
for i in range(1, N + 1):
    book_title = data[i]
    if book_title in book_count:
        book_count[book_title] += 1
    else:
        book_count[book_title] = 1

# 가장 많이 팔린 책 제목 찾기
max_count = 0
most_sold_book = ""

for title, count in book_count.items():
    # 최대 빈도 업데이트 및 사전 순 정렬
    if count > max_count or (count == max_count and title < most_sold_book):
        max_count = count
        most_sold_book = title

print(most_sold_book)