array = list(map(int, input().split()))

idx_999 = array.index(999) if 999 in array else array.index(-999)
a = array[0:idx_999]

print(f"{max(a)} {min(a)}")