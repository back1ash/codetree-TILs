import sys
input = sys.stdin.readline

n = int(input())
grades = []
for _ in range(n):
    grades.append(list(map(int, input().split())))

num_pass = 0
for person in grades:
    if sum(person)/4 >= 60:
        print("pass")
        num_pass += 1
    else:
        print("fail")

print(num_pass)