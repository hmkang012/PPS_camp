# B104 숫자카드
# 1. N 입력 받기
# 1-2. N개의 원소들을 List에 넣기
# 2. M 입력 받기
# 2-2. M개의 원소들을 list에 넣기
# 3. M_list에 있는 값들이 N_list에 있는지 확인
# 4. 있으면 1, 없으면 0을 출력하기

n_list = []
m_list = []
result = [] # 결과(0, 1) 저장

N = int(input())
n_list = list(map(int, input().split()))

M = int(input()) # M과 관련된 것들 받기
m_list = list(map(int, input().split()))

# n_list를 set으로 변환하여 탐색 시간 단축하기
n_set = set(n_list)

for i in m_list:
    if i in n_set: # 있으면 1
        result.append(1)
    else: # 없으면 0
        result.append(0)

print(" ".join(map(str, result)))