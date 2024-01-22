array = list(map(int, input().split()))

for i in range(8):
    array.append(array[-1] + (2*array[-2]))

print(" ".join(map(str, array)))