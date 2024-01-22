n = int(input())

count_5 = 0 if n%5 !=0 else 1
array = [n]

i = 2
while count_5 < 2:
    nxt = n*i
    i += 1
    array.append(nxt)
    if nxt % 5 == 0:
        count_5 += 1

print(" ".join(map(str, array)))