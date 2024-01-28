import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
square = [list(map(int, input().split())) for _ in range(n)]
k = k-1

for row in range(n):
    flag = 0
    for a in range(m):
        if square[row][k+a] != 0:
            square[row-1][k:k+m] = [1 for _ in range(m)]
            flag = 1
            break
    if flag == 1:
        break

for row in square:
    print(' '.join(map(str, row)))