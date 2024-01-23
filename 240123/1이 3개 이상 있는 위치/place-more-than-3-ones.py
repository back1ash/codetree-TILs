import sys
input = sys.stdin.readline

n = int(input())
square = []

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for _ in range(n):
    row = list(map(int, input().split()))
    square.append(row)

dx = [0,1,0,-1]
dy = [1,0,-1,0]

result = 0

for i in range(n):
    count = 0
    for j in range(n):
        for a,b in zip(dx, dy):
            x = i + a
            y = j + b
            if in_range(x,y) and square[x][y] == 1:
                count += 1
    if count >= 3:
        result += 1

print(result)