import sys
input = sys.stdin.readline

int_list = list(map(int, input().split()))
tmp = []

for num in int_list:
    if num >= 250:
        break
    tmp.append(num)

print(f"{sum(tmp)} {sum(tmp)/len(tmp):.1f}")