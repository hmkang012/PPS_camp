# 선수 수 입력 받기
n = int(input())

# 각 선수의 성 입력 받긔
names = []
for _ in range(n):
    name = input().strip()
    names.append(name)

# 성의 첫 글자를 세는 딕셔너리 선언
first_letters = {}

# 각 성의 첫 글자를 세기
for name in names:
    first_letter = name[0]
    if first_letter in first_letters:
        first_letters[first_letter] += 1
    else:
        first_letters[first_letter] = 1

result = [] # 결과 넣을 리스트

# 다섯 명 이상인 첫 글자만 결과 리스트에 추가
for letter, count in first_letters.items():
    if count >= 5:
        result.append(letter)

# 출력~~
if result:
    print(''.join(sorted(result)))
else:
    print("PREDAJA")
