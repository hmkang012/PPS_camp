# 1. 첫번째 줄에 입력하는 테스트 케이스 T input
# - T만큼 반복문 반복
# - for _ in range(T)로 사용하면 되지 않을까?

# 2. for문 안에서
# - 숫자 입력 받고, map을 사용해서 한 줄에 입력받은 두 개의 정수를 각각 변수에 저장될 수 있게 한다.
# - A, B = map(int, input().split())

# 3. 각 케이스 별 결과값(A+B)을 출력한다.

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    print(A+B)