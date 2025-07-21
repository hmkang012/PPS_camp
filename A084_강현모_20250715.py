import sys
input = sys.stdin.read

# 문자열 ㅇ릭기
S = input().strip()

# 모든 접미사를 생성하여 리스트에 저장
suffixes = [S[i:] for i in range(len(S))]

# 접미사를 사전순으로 정렬
suffixes.sort()

for suffix in suffixes:
    print(suffix)