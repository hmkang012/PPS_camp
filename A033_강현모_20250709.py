num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
num3 = list(map(int, input().split()))
num4 = list(map(int, input().split()))
num5 = list(map(int, input().split()))

#num마다 sum구하기
sum1 = sum(num1)
sum2 = sum(num2)
sum3 = sum(num3)
sum4 = sum(num4)
sum5 = sum(num5)

# 큰 수 구하기
list_a = [sum1, sum2, sum3, sum4, sum5]
max_value = max(list_a)

#결과 출력
print (list_a.index(max_value)+1)
print (max_value)