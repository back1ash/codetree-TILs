a = input()
b = input()
c = input()

result = []
result.append(len(a))
result.append(len(b))
result.append(len(c))

print(f"{max(result)-min(result)}")