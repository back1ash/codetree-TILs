k, n = map(int, input().split())
answer = []

def print_answer(a):
    print(' '.join(map(str, a)))

def choose(curr_num):
    if curr_num == n+1:
        print_answer(answer)
        return
    for i in range(1,n+1):
        answer.append(i)
        choose(curr_num + 1)
        answer.pop()

    return

choose(1)