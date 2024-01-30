n = int(input())

dp =[0 for _ in range(n + 1)]
dp[0] = 1
for i in range(1, n + 1):
    for num in range(1, 5):
        if i - num >= 0:
            dp[i] += dp[i - num]

print(dp[n])