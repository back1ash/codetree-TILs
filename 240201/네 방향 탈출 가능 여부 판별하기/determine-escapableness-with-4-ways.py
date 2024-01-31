from collections import deque
import sys
input = sys.stdin.readline

def solve():
    q = deque()
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1 ,1]

    n,m = map(int, input().split())
    maze = [list(map(int, input().split())) for _ in range(m)]
    if maze[m-1][n-1] == 1:
        print(0)
        return

    def in_range(x, y):
        return 0<=x<m and 0<=y<n

    def bfs():
        while q:
            x, y = q.popleft()
            for dx, dy in zip(dxs, dys):
                if in_range(x+dx, y+dy) and not maze[x+dx][y+dy]:
                    q.append([x+dx, y+dy])
                    maze[x+dx][y+dy] = 1
    q.append([0,0])
    bfs()
    print(1 if maze[m-1][n-1] == 1 else 0)

solve()