n, t = map(int, input().split())

direction = {"U": 0, "D" : 3, "R": 1, "L":2}
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
x,y,d = input().split()
x = int(x)
y = int(y)
d = direction[d]

def in_range(x,y):
    return 1 <= x <= n and 1 <= y <= n

for i in range(t):
    cx = x + dx[d]
    cy = y + dy[d]
    if not in_range(cx,cy):
        d = (3 - d) % 4
    else:
        x = cx
        y = cy

print(y-1, x-1)