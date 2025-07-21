num = [] # 숫자들 받을 
result = [] # 결과를 return 할 배열

N = int(input()) # N 입력 ㅂ다기
num = input() # 숫자 입력 받기

int_num_list = list(map(int, num.split())) #입력 받은 숫자를 int형태의 List화 하기
# print (int_num_list) #확인

for value in int_num_list: # 중복 지우기
    if value not in result:
        result.append(value)

result = sorted(result)
print(" ".join(map(str, result))) # 문자열로 구분하고, 하나의 문자열로 공백 포함해서 합쳐서 출력