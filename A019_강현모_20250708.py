A = int(input())
B = int(input())
C = int(input())
count = [0]*10

result = A*B*C # 3개의 정수 곱한 결과
num_list = list(map(int, str(result))) #list로 변환

for i in range(0, 10, 1):
    print (num_list.count(i))
