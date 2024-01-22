a, b = map(int, input().split())

count = [0 for _ in range(b)]
result = 0

def square(x):
    return x**2

while a>1:
    a, remainder = divmod(a, b)
    count[remainder] += 1

print(sum(map(square, count)))