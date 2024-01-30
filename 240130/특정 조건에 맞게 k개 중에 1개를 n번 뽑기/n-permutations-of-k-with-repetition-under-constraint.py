k, n = map(int, input().split())
answer = []

def print_answer(a):
     for elem in a:
        print(' '.join(map(str, a)))

curr_num = 1
def choose(curr_num):
    if curr_num == n+1:
        print_answer(answer)
        return
    for i in range(1,k+1):
        answer.append(i)
        choose(curr_num + 1)
        answer.pop()

choose(1)