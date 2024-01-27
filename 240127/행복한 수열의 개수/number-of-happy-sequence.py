n, m = map(int, input().split())

def in_range(x, y):
    return 0<=x<n and 0<=y<n

square = [list(map(int, input().split())) for _ in range(n)]

happy = 0
for y in range(n):
    for x in range(n):
        crnt = square[y][x]
        x_count = 0
        for dx in range(m):
            if not in_range(x+dx, y):
                break
            if square[y][x+dx] != crnt:
                break
            x_count += 1
        if x_count >= m:
            happy += 1
            break



for x in range(n):
    for y in range(n):
        crnt = square[y][x]
        y_count = 0
        for dy in range(m):
            if not in_range(x, y+dy):
                break
            if square[y+dy][x] != crnt:
                break
            y_count += 1
        if y_count >= m:
            happy += 1
            break
        
print(happy)