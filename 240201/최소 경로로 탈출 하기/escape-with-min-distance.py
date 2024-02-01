from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
q = deque()
step = [[-1 for _ in range(m)] for _ in range(n)]
step[0][0] = 0

dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]

def in_range(x, y):
    return 0<=x<n and 0<=y<m

def visited(x, y):
    return step[x][y] != -1

def shorter(a, b):
    return b if a == -1 else min(a,b)

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            cx, cy = (x+dx, y+dy)
            if in_range(cx, cy) and maze[cx][cy] == 1:
                if not visited(cx, cy):
                    q.append([cx, cy])
                step[cx][cy] = shorter(step[cx][cy], step[x][y] + 1)
                
def answer():
    print(step[-1][-1])

q.append([0,0])
bfs()
answer()