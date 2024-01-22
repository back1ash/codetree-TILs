n = int(input())
array = list(map(int, input().split()))

min_diff = 999
for i in range(n):
    if i == n-1:
        break
    for j in range(i+1,n):
        if array[j] - array[i] < min_diff:
            min_diff = array[j] - array[i]

print(min_diff)