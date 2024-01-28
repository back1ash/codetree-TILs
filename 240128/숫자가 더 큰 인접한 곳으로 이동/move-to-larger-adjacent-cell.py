import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())
r, c = (r-1, c-1)
def in_range(x, y):
    return 0<=x<n and 0<=y<n

square = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visit_list = []
while True:
    direction = 4
    now = square[r][c]
    visit_list.append(now)
    for i in range(4):
        if in_range(c+dx[i], r+dy[i]) and now < square[r+dy[i]][c+dx[i]]:
            now = square[r+dy[i]][c+dx[i]]
            direction = i
            break
    if direction == 4:
        break

    r, c = (r+dy[direction], c+dx[direction])

print(' '.join(map(str, visit_list)))