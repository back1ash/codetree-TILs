import sys
input = sys.stdin.readline

result = 0
for i in range(4):
    array = list(map(int, input().split()))
    result += sum(array[0:i+1])

print(result)