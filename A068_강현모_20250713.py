from collections import deque
import sys
input = sys.stdin.read


data = input().strip().split('\n')

n = int(data[0])

queue = deque() # queue 구현하는 deque()

result = []

for i in range(1, n + 1):
    command = data[i]
    
    if command.startswith("push"):
        _, x = command.split()
        queue.append(int(x))
    elif command == "pop":
        if queue:
            result.append(queue.popleft())
        else:
            result.append(-1)
    elif command == "size":
        result.append(len(queue))
    elif command == "empty":
        if queue:
            result.append(0)
        else:
            result.append(1)
    elif command == "front":
        if queue:
            result.append(queue[0])
        else:
            result.append(-1)
    elif command == "back":
        if queue:
            result.append(queue[-1])
        else:
            result.append(-1)

sys.stdout.write('\n'.join(map(str, result)) + '\n')