n = int(input())

array = list(map(int, input().split()))
idxs = []
while array:
    biggest = max(array)
    index = array.index(biggest)
    array = array[0:index]
    idxs.append(index+1)

print(' '.join(map(str, idxs)))