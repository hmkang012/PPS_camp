h, m = map(int, input().split()) # hour, min

m -= 45

if (m<0):
    m += 60
    h -= 1
    if (h < 0):
        h = 23

print (f'{h} {m}')