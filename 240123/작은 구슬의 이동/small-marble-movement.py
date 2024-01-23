n, t = map(int, input().split())

direction = {"U": 0, "D" : 3, "R": 1, "L":2}
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
y,x,d = input().split()
x = int(x)
y = int(y)
d = direction[d]

def in_range(x,y):
    return 1 <= x <= n and 1 <= y <= n

for i in range(t):
    cx = x + dx[d]
    cy = y + dy[d]
    if in_range(cx,cy):
        x = cx
        y = cy
    else:
        d = (3 - d)

print(y, x)