import sys
input = sys.stdin.readline

n = int(input())
array = input().split()

def is_even(x):
    if int(x)%2 == 0:
        return True
    else:
        return False

even = list(filter(is_even, array))

print(" ".join(reversed(even)))