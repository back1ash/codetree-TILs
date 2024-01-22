n = int(input())

array = list(map(int, input().split()))
array.sort(reverse=True)

print(array[0],array[1])