import sys
input = sys.stdin.readline

array = list(map(int, input().split()))
mul_2 = []

for i in array:
    if i == 0:
        break
    if i%2 == 0:
        mul_2.append(i)

print(f"{len(mul_2)} {sum(mul_2)}")