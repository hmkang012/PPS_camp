num_list = []

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    # print (A, B)

    if A <= B: # 범위 설정
        div_num = B
    elif A >= B:
        div_num = A
    
    num_list.clear()  # 공약수를 찾기 전에 리스트 초기화


    for i in range(1, div_num+1): # 공약수 구하기
        if (A % i == 0) and (B % i == 0):
            num_list.append(i)

    max_div_num = max(num_list) # 최대 공약수 구하기
    # print (max_div_num) # 최대 공약수 출력

    result = (A * B) // max_div_num
    print (result)