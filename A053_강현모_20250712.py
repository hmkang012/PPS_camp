from collections import deque
import sys

input = sys.stdin.readline
print = sys.stdout.write

stack = deque()

def push(x):
    stack.append(x)

def pop():
    if stack:
        print(f"{stack.pop()}\n")
    else:
        print("-1\n")

def size():
    print(f"{len(stack)}\n")

def empty():
    print("1\n" if not stack else "0\n")

def top():
    if stack:
        print(f"{stack[-1]}\n")
    else:
        print("-1\n")

n = int(input())

for _ in range(n):
    command = input().split()
    
    if command[0] == "push":
        push(int(command[1]))
    elif command[0] == "pop":
        pop()
    elif command[0] == "size":
        size()
    elif command[0] == "empty":
        empty()
    elif command[0] == "top":
        top()