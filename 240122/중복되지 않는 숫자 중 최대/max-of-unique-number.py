n = int(input())
array = list(map(int, input().split()))
array.sort()

biggest = -1

for cur in array:
    if biggest < cur:
        count = 0
        for e in array:
            if e == cur:
                count += 1
        
        if count == 1:
            max_num = cur

print(max_num)