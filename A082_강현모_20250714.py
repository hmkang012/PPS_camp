n = int(input())
people = []

for _ in range(n):
    age, name = input().split()
    people.append([int(age), name])

for i in sorted(people, key=lambda p_name : p_name[0]):
    print (i[0], i[1])