# A022 핸드폰요금

N = int(input()) # 개수 입력 받기
call_time = list(map(int, input().split()))

y = 0 # 영식 요금제
m = 0 # 민식 요금제

for i in call_time: # list에 있는 값들 계산하기
    y += (i//30+1)*10 # 영식 요금제 계산
    m += (i//60+1)*15 # 민식 요금제 계산

if y > m:
    print ("M", m)
elif y == m:
    print("Y M", y)
elif y < m:
    print ("Y", y)