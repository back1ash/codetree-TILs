n = int(input())
array = list(map(int, input().split()))

max_profit = 0
for i in range(n):
    for j in range(i,n):
        if array[j] - array[i] > max_profit:
            max_profit = array[j] - array[i]

print(max_profit)