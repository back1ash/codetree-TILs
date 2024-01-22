import sys
input = sys.stdin.readline

clinic = [0 for _ in range(4)]

for i in range(3):
    cold, temp = input().split()
    temp = int(temp)
    if cold == "Y":
        if temp >= 37:
            clinic[0] += 1
        else:
            clinic[2] += 1
    else:
        if temp >= 37:
            clinic[1] += 1
        else:
            clinic[3] += 1

result = " ".join(map(str, clinic))
if clinic[0] >= 2:
    result += " E"
print(result)