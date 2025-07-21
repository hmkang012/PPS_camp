n= int(input())

for _ in range(n):
    case = input() # o, x 입력
    score = 0
    current_streak = 0
    for char in case:
        if char == 'O':
            current_streak += 1
            score += current_streak
        else:
            current_streak = 0
    print(score)
