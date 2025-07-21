str = input() #카이사르 단어

list = list(str)

return_word = []

for i in range(len(str)):
    if list[i] == "D":
        return_word.append("A")
    elif list[i] == "E":
        return_word.append("B")
    elif list[i] == "F":
        return_word.append("C")
    elif list[i] == "G":
        return_word.append("D")
    
    elif list[i] == "H":
        return_word.append("E")
    elif list[i] == "I":
        return_word.append("F")
    elif list[i] == "J":
        return_word.append("G")

    elif list[i] == "K":
        return_word.append("H")
    elif list[i] == "L":
        return_word.append("I")
    elif list[i] == "M":
        return_word.append("J")
    elif list[i] == "N":
        return_word.append("K")
    elif list[i] == "O":
        return_word.append("L")
    elif list[i] == "P":
        return_word.append("M")

    elif list[i] == "Q":
        return_word.append("N")
    elif list[i] == "R":
        return_word.append("O")
    elif list[i] == "S":
        return_word.append("P")
    elif list[i] == "T":
        return_word.append("Q")
    elif list[i] == "U":
        return_word.append("R")
    elif list[i] == "V":
        return_word.append("S")
    elif list[i] == "W":
        return_word.append("T")
    elif list[i] == "X":
        return_word.append("U")

    elif list[i] == "Y":
        return_word.append("V")
    elif list[i] == "Z":
        return_word.append("W")
    elif list[i] == "A":
        return_word.append("X")
    elif list[i] == "B":
        return_word.append("Y")
    elif list[i] == "C":
        return_word.append("Z")
    
print ("".join(return_word))