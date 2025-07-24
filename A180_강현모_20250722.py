num = input()
A, B, C= map(int, num.split())

print ((A+B)%C)
print (((A%C) + (B%C))%C)
print ((A*B)%C)
print ((A%C) * (B%C)%C)