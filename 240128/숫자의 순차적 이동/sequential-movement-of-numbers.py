import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def in_range(x, y):
    return 0<=x<n and 0<=y<n

square = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(m):
    crnt = 1
    while crnt <= n**2:
        flag = 0
        for i in range(n):
            for j in range(n):
                if square[i][j] == crnt:
                    biggest = 0
                    direction = 0
                    for a in range(8):
                        if in_range(i+dy[a], j+dx[a]) and square[i+dy[a]][j+dx[a]] > biggest:
                            direction = a
                            biggest = square[i+dy[a]][j+dx[a]]
                    square[i+dy[direction]][j+dx[direction]] = square[i][j]
                    square[i][j] = biggest
                    flag = 1
                    break
            if flag == 1:
                break
        crnt += 1

for row in square:
    print(' '.join(map(str, row)))