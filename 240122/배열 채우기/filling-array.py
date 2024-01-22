import sys
input = sys.stdin.readline

a = []
array = input().split()
for x in array:
    if x == "0":
        break
    a.append(x)

print(" ".join(reversed(a)))