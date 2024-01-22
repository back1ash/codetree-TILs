import sys
input = sys.stdin.readline

array1 = []
array2 = []

for i in range(3):
    row = list(map(int, input().split()))
    array1.append(row)

input()

for i in range(3):
    row = list(map(int, input().split()))
    array2.append(row)

result = []
for x in range(3):
    row = []
    for y in range(3):
        row.append(array1[x][y] * array2[x][y])
    result.append(row)

for row in result:
    print(" ".join(map(str, row)))