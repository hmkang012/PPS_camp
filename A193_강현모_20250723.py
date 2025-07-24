# - 4를 입력 하면 long int
# - 8이면 long long int
# - 16이면 long long long long int
# - 20이면 long long long long long int

# 그러면...
# 1. 숫자를 입력 받기
# 2. 입력 받은 숫자를 4로 나눴을 때 몫이 얼마인지 확인
# 3. 그 몫만큼 Long을 출력하고 int를 출력하기

result = []
N = int(input())

num = N//4
# print (num)

for i in range(num):
    result.append('long ')

output = ''.join(result) + "int"
print(output)