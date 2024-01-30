import copy

n, m, k = map(int, input().split())
distance = list(map(int, input().split()))

# global orders
orders = []

def set_order(order):
    if len(order) == n:
        orders.append(copy.deepcopy(order))
        return
    for i in range(k):
        order.append(i)
        set_order(order)
        order.pop()

def above_m(x):
    return x>=m

def score(order):
    idx = 0
    tokens = [0 for _ in range(k)]
    for x in order:
        tokens[x] += distance[idx]
        idx += 1
    array = list(filter(above_m, tokens))
    return len(array)

def max_score():
    result = 0
    for order in orders:
        now = score(order)
        result = now if now > result else result
    print(result)

set_order([])
max_score()