n, m = map(int, input().split())

def in_range(x, y):
    return 0<=x<m and 0<=y<n

rectangle = [[0 for _ in range(m)] for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x,y = (0, 0)
direction = 0

rectangle[0][0] = 1
crnt = 2
while crnt <= n*m:
    cx, cy = (x+dx[direction], y+dy[direction])
    if not in_range(cx, cy) or rectangle[cy][cx] != 0:
        direction = (direction + 1) % 4
    else:
        x, y = (cx, cy)
        rectangle[y][x] = crnt
        crnt += 1

for row in rectangle:
    print(" ".join(map(str, row)))