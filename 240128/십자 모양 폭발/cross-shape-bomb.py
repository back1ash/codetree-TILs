import sys
input = sys.stdin.readline

n = int(input())

def in_range(x, y):
    return 0<=x<n and 0<=y<n

square = [list(map(int, input().split())) for _ in range(n)]

r, c = map(int, input().split())
r, c = (r-1, c-1)
scope = square[r][c]
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

#boom
for a in range(scope):
    for i in range(4):
        if in_range(r+(dx[i]*a), c+(dy[i]*a)):
            square[r+(dx[i]*a)][c+(dy[i]*a)] = 0

tmp = [[0 for _ in range(n)]for _ in range(n)]
#gravity
for x in range(n):
    cur = n-1
    for y in range(n-1, -1, -1):
        if square[y][x] != 0:
            tmp[cur][x] = square[y][x]
            cur -= 1

square = tmp
for row in square:
    print(' '.join(map(str, row)))