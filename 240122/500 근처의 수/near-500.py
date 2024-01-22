def discriminant_neg(x):
    return x<0
def discriminant_pos(x):
    return x>0


array = list(map(int, input().split()))

array = [e-500 for e in array]
array.sort()

neg_array = list(filter(discriminant_neg, array))
pos_array = list(filter(discriminant_pos, array))

print(f"{neg_array[-1]+500} {pos_array[0]+500}")