n = int(input())

array = [1, n]
while array[-1] < 100:
    array.append(array[-2] + array[-1])

print(" ".join(map(str, array)))