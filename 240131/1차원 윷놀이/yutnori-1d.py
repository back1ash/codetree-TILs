n, m, k = map(int, input().split())
distance = list(map(int, input().split()))

# global orders
orders = []

def set_order(order):
    if len(order) == n:
        orders.append(order.copy())
        return
    for i in range(k):
        order.append(i)
        set_order(order)
        order.pop()

def above_m(x):
    return x>=m

def score(order):
    idx = 0
    tokens = [1 for _ in range(k)]
    for x in order:
        tokens[x] += distance[idx]
        idx += 1
    return len(list(filter(above_m, tokens)))

def max_score():
    result = 0
    for order in orders:
        now = score(order)
        result = now if now > result else result
    print(result)

set_order([])
max_score()