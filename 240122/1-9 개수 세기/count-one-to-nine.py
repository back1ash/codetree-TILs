n = int(input())
count = [0 for _ in range(1,10)]

inpt =  list(map(int, input().split()))

for i in inpt:
    count[i-1] += 1

for x in count:
    print(x)