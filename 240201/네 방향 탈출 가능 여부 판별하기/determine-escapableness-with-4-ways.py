from collections import deque
import sys
input = sys.stdin.readline

q = deque()
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1 ,1]

n,m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(m)]
maze[0][0] = 0

def in_range(x, y):
    return 0<=x<m and 0<=y<n

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            cx, cy = (x+dx, y+dy)
            if in_range(cx, cy) and maze[cx][cy]:
                q.append([cx, cy])
                maze[cx][cy] = 0
q.append([0,0])
bfs()
print(1 if maze[-1][-1] == 0 else 0)