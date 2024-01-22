f_list = input().split()

def fibonacci(x, y):
    return str((int(x)+int(y))%10)

for i in range(8):
    f_list.append(fibonacci(f_list[-2], f_list[-1]))

print(' '.join(f_list))