n = int(input())

square = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

max_coin = 0
for i in range(n):
    for j in range(n):
        count = 0
        for dx in range(3):
            for dy in range(3):
                if in_range(j+dx, i+dy) and square[i+dy][j+dx]:
                    count += 1
    
        max_coin = max(max_coin, count)

print(max_coin)