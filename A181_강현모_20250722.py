num1 = int(input())
num2 = int(input())

num2_1 = int((num2%100)%10) #일의자리
num2_10 = int((num2%100)/10)# 십의자리
num2_100 = int(num2/100) # 백의자리

# print (num2_100, num2_10, num2_1)

print (num1*num2_1)
print (num1* num2_10)
print (num1*num2_100)

print(num1*num2)