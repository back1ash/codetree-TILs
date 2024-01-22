attempts = list(map(int, input().split()))
count = [0 for _ in range(7)]

for e in attempts:
    count[e] += 1

for x in range(1,7):
    print(f"{x} - {count[x]}")