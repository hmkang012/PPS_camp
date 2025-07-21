T = int(input()) # test case


for _ in range(T):
    form = list(map(str, input().split())) # input of forms
    result = 0 # answer
    for i in range(len(form)):
        if i == 0:
            result = float(form[i])
        else:
            if form[i] == "@":
                result *= 3
            elif form[i] == "%":
                result += 5
            elif form[i] == "#":
                result -= 7
    print ("%0.2f" % result)