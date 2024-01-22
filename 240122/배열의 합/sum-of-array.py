import sys
input = sys.stdin.readline

results = []
for i in range(4):
    array = list(map(int, input().split()))
    results.append(sum(array))

for result in results:
    print(result)