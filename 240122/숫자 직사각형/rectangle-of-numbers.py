n, m = map(int, input().split())

cur = 1
array_2 = []
for i in range(n):
    array_1 = []
    for _ in range(m):
        array_1.append(cur)
        cur += 1
    array_2.append(array_1)

for array in array_2:
    print(" ".join(map(str, array)))