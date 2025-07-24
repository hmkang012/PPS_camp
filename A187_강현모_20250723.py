# A187 윤년

year = int(input().strip())

if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0): # 윤년 여부 판단
    print("1")
else:
    print("0")