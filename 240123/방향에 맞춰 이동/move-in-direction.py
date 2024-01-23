import sys
input = sys.stdin.readline

n = int(input())
x, y = (0,0)
for i in range(n):
    direction, distance = input().split()
    distance = int(distance)
    if direction == "N":
        y += distance
    elif direction == "E":
        x += distance
    elif direction == "S":
        y -= distance
    elif direction == "W":
        x -= distance

print(x,y)