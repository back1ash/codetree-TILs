n, t = map(int, input().split())

belts = [list(map(int, input().split())) for _ in range(3)]

now = 0
while now < t:
    tmp = [belts[x][-1] for x in range(3)]
    for i in range(3):
        for j in range(n-1,0,-1):
            belts[i][j] = belts[i][j-1]
    for i in range(3):
        belts[i][0] = tmp[i-1]
    now += 1

for belt in belts:
    print(" ".join(map(str, belt)))