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

def score(order):
    idx = 0
    tokens = [1 for _ in range(k)]
    for x in order:
        if tokens[x] > m:
            return 0
        tokens[x] += distance[idx]
        idx += 1
    count = 0
    for token in tokens:
        if token >= m:
            count += 1
    return count

def max_score():
    result = 0
    for order in orders:
        now = score(order)
        result = now if now > result else result
    print(result)

set_order([])
max_score()