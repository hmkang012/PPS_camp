def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            return True
    return False

test_cases = ["a234", "1234", "12345", "123456"]
for s in test_cases:
    print(solution(s))