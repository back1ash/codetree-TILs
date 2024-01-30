k, n = map(int, input().split())
answer = []

def print_answer(a):
     print(' '.join(map(str, a)))
     return

curr_num = 1
def choose(curr_num):
    if curr_num == n+1:
        print_answer(answer)
        return
        
    for i in range(1,k+1):
        answer.append(i)
        if len(answer) >= 3 and i == answer[-2] == answer[-3]:
            answer.pop()
            continue
        choose(curr_num + 1)
        answer.pop()

choose(1)