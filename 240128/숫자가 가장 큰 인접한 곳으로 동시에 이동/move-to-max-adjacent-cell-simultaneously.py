n, m, t = map(int, input().split())

square = [list(map(int, input().split())) for _ in range(n)]

marbles = [list(map(int, input().split())) for _ in range(m)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

for time in range(t):
    count = [[0 for _ in range(n)] for _ in range(n)]
    for x,y in marbles:
        x, y = (x-1, y-1)
        biggest = 0
        direction = 0
        for i in range(4):
            if in_range(x+dx[i], y+dy[i]) and square[y+dy[i]][x+dx[i]] < biggest:
                direction = i
        count[y+dy[direction]][x+dx[direction]] += 1

    new_marble = []
    for i in range(n):
        for j in range(n):
            if count[i][j] >= 2:
                count [i][j] = 0
            elif count[i][j] == 1:
                new_marble.append([j, i])
    marbles = new_marble

print(len(marbles))