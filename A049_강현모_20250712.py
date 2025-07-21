import sys
input = sys.stdin.read

# Read input
data = input().splitlines()

vowels = 'aeiou'

for password in data:
    if password == 'end':
        break
    
    contains_vowel = False
    consecutive_vowels = 0
    consecutive_consonants = 0
    acceptable = True
    
    for i in range(len(password)):
        if password[i] in vowels:
            contains_vowel = True
            consecutive_vowels += 1
            consecutive_consonants = 0
        else:
            consecutive_vowels = 0
            consecutive_consonants += 1
        
        if consecutive_vowels >= 3 or consecutive_consonants >= 3:
            acceptable = False
            break
    
    for i in range(1, len(password)):
        if password[i] == password[i-1] and password[i] not in ('e', 'o'):
            acceptable = False
            break
    
    if not contains_vowel:
        acceptable = False
    
    if acceptable:
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")