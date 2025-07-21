import sys
input = sys.stdin.read

data = input().strip().split('\n')
N = int(data[0])
serial_numbers = data[1:]

def sum_of_digits(s):
    return sum(int(c) for c in s if c.isdigit())

# 정렬 조건에 따른 비교..
serial_numbers.sort(key=lambda x: (len(x), sum_of_digits(x), x))

for serial in serial_numbers:
    print(serial)
