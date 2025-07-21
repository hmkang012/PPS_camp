N = int(input())
num = int(input())


if N > 5:
    print ("Love is open door")
else:
    for i in range(N-1):
        if num == 0:
            print (1)
            num = 1
        else:
            print(0)
            num = 0