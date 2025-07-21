def solution(arr, divisor):
    a_list = []
    
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            a_list.append(arr[i])
    
    if not a_list:
        return [-1]
    
    return sorted(a_list)

test_case = [([5, 9, 7, 10], 5), ([2, 36, 1, 3], 1), ([3, 2, 6], 10)]
for arr, divisor in test_case:
    print(solution(arr, divisor))
