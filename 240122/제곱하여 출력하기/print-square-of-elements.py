import sys
input = sys.stdin.readline

def square(x):
    return str(x**2)

n = int(input())
array = list(map(int, input().split()))

pow_array = map(square, array)

print(' '.join(pow_array))