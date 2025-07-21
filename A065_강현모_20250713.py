import sys
input = sys.stdin.read

data = input().strip().split('\n')

N = int(data[0])

# 두 번째 줄부터 N개의 줄에 걸쳐 i번 점의 위치 xi, yi
points = []
for i in range(1, N + 1):
    x, y = map(int, data[i].split())
    points.append((x, y))

# 점들을 x좌표가 증가하는 순으로
# x좌표가 같으면 y좌표가 증가하는 순서로 정렬!
points.sort()

for point in points:
    print(point[0], point[1])
