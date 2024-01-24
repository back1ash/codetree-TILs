n, t = map(int, input().split())
r, c, d = input().split()
r, c = (int(r)-1, int(c)-1)
direction = {'U':1, 'D':2, 'R':0, 'L':3}
d = direction[d]

def in_range(x, y):
    return 0<=x<n and 0<=y<n


dx = [1, 0, 0 ,-1]
dy = [0, -1, 1 ,0]

now = 0
while now < t:
    cx, cy = (c+dx[d], r+dy[d])
    if not in_range(cx, cy):
        d = (3-d) % 4
    else:
        c, r = (cx, cy)
    now += 1

print(r+1, c+1)