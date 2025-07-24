N, M = map(int, input().split()) # A, B 집합의 개수

A = []
B = []

A = list(map(int, input().split()))[:N] # N개의 요소를 입력받기
B = list(map(int, input().split()))[:M] # M개의 요소 입력받기

setA = set(A) #list를 set으로 바꾸기
setB = set(B)

comlementAB = setA - setB
comlementBA = setB - setA

union = comlementAB | comlementBA
print (len(union))