array = input().split()

def under_10(x):
    if int(x)<10:
        return False
    else:
        return True

idx_0 = array.index("0")
a = array[0:idx_0]
a = list(filter(under_10, a))
count = [0 for _ in range(10)]

for i in a:
    count[int(i[0])] += 1

for x in range(1,10):
    print(f"{x} - {count[x]}")