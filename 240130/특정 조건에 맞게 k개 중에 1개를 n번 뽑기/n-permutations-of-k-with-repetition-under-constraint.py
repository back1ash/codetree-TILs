k, n = map(int, input().split())
answer = []

def print_answer(a):
     print(' '.join(map(str, a)))
     return

def same_check(array):
    return len(set(array)) == 1

curr_num = 1
def choose(curr_num):
    if curr_num == n+1:
        if not same_check(answer):
            print_answer(answer)
        return
    for i in range(1,k+1):
        answer.append(i)
        choose(curr_num + 1)
        answer.pop()

choose(1)