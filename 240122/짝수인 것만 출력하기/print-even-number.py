n = int(input())

def is_even(x):
    if int(x)%2 == 0:
        return True
    else:
        return False

array = input().split()
even_list = list(filter(is_even, array))

print(' '.join(even_list))