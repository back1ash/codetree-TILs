n,t = map(int, input().split())

belts = [list(map(int, input().split())) for _ in range(2)]

now = 0
while now < t:
    tmp = [belts[0][-1], belts[1][-1]]
    for a in range(2):
        for i in range(n-1,0,-1):
            belts[a][i] = belts[a][i-1]
    belts[1][0], belts[0][0] = tmp 
    now += 1

for belt in belts:
    print(" ".join(map(str, belt)))