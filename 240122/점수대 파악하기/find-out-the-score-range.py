def under_10(x):
    if int(x) < 10:
        return False
    else:
        return True

grades = input().split()

idx_0 = grades.index("0")
a = list(filter(under_10, grades[0:idx_0]))
count = [0 for _ in range(11)]

for grade in grades:
    if grade == "100":
        count[10] += 1
        continue
    count[int(grade[0])] += 1

for x in range(10,0,-1):
    print(f"{x}0 - {count[x]}")