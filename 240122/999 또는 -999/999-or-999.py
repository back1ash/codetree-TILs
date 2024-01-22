array = list(map(int, input().split()))

idx_999 = array.index(999) if array.index(999) else array.index(-999)
a = array[0:idx_999]

print(f"{max(a)} {min(a)}")