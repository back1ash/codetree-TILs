import sys
input = sys.stdin.readline

a = []
array = list(map(int, input().split()))

for i in array:
    if i == 0:
        break
    a.append(i)

print(f"{sum(a)} {sum(a)/len(a):.1f}")