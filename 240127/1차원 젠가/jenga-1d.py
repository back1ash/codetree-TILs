import sys
input = sys.stdin.readline

n = int(input())

blocks = [int(input()) for _ in range(n)]

s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

tmp = blocks[:s1-1] + blocks[e1:]
blocks = tmp
tmp = blocks[:s2-1] + blocks[e2:]
blocks = tmp

print(len(blocks))
print('\n'.join(map(str, blocks)))