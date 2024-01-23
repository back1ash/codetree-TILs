commands = input()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0
x,y = (0,0)

for command in commands:
    if command == "L":
        direction -= 1
    elif command == "R":
        direction += 1
    elif command == "F":
        x += dx[direction]
        y += dy[direction]
print(x,y)