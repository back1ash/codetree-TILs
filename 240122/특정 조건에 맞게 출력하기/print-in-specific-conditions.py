array = input().split()
a = []

def process(x):
    x = int(x)
    if x%2 == 0:
        return x//2
    else:
        return x+3

index_0 = array.index("0")
a = array[0:index_0]

result = list(map(process, a))
print(" ".join(map(str, result)))