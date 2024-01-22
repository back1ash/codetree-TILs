array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

print(f"{sum(array1)/4:.1f} {sum(array2)/4:.1f}")
print(f"{(array1[0]+array2[0]) / 2:.1f} {(array1[1]+array2[1]) / 2:.1f} {(array1[2]+array2[2]) / 2:.1f} {(array1[3]+array2[3]) / 2:.1f}")
print(f"{(sum(array1)+sum(array2))/8:.1f}")