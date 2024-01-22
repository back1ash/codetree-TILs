n = int(input())
array = list(map(int, input().split()))

print(f"{min(array)} {array.count(min(array))}")