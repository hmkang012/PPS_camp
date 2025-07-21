# - 1부터 4까지 역 순서대로 내린 사람 수, 탄 사람 수 입력받기
# - 총 list를 4개를 만들고, index가 0인 경우에는 -를 붙여 음수로 만든다.
# - 1->2, 2->3, 3->4 일 때의 총 사람 숫자를 저장한다.
# - 1->2, 2->3, 3->4의 사람 숫자를 list에 저장하고 max값을 뽑는다.

#input
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
num3 = list(map(int, input().split()))
num4 = list(map(int, input().split()))

# 각 역마다의 사람 숫자 total 계산하기
sum1 = num1[0] + num1[1]
sum_1_to_2 = sum1 - num2[0] + num2[1]
sum_2_to_3 = sum_1_to_2 - num3[0] + num3[1]
sum_3_to_4 = sum_2_to_3 - num4[0] + num4[1]

result_list = [sum1, sum_1_to_2, sum_2_to_3, sum_3_to_4] #max를 구하기 위해 list로 만들기
print (max(result_list))