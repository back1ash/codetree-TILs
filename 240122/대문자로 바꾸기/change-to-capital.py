import sys
input = sys.stdin.readline

def upper(c):
    return c.upper()
for _ in range(5):
    array = list(map(upper, input().split()))
    print(" ".join(array))