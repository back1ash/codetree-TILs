import sys
input = sys.stdin.readline

n, m = map(int, input().split())

array1 = []
for _ in range(n):
    row = list(map(int, input().split()))
    array1.append(row)

array2 = []
for _ in range(n):
    row = list(map(int, input().split()))
    array2.append(row)

for i in range(n):
    row = []
    for j in range(m):
        if array1[i][j] == array2[i][j]:
            row.append(0)
        else:
            row.append(1)
    print(' '.join(map(str, row)))