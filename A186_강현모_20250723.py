# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

score = int(input())

if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score <=89:
    print("B")
elif score >= 70 and score <=79:
    print("C")
elif score >= 60 and score <= 69:
    print("D")
else:
    print("F")