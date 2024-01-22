import sys
input = sys.stdin.readline

n = int(input())
grades = list(map(float, input().split()))

avg = round(sum(grades) / len(grades), 1)

print(avg)
if avg > 4.0:
    print("Perfect")
elif avg >= 3.0:
    print("Good")
elif avg < 3.0:
    print("Poor")