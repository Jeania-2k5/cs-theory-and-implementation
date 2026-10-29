# 9) 0/1 Knapsack (Dynamic Programming)

weights = [1, 3, 4, 5]
profits = [1, 4, 5, 7]
capacity = 7

n = len(weights)

# DP table with (n+1) rows and (capacity+1) columns
dp = []
for i in range(n + 1):
    row = [0] * (capacity + 1)
    dp.append(row)

for i in range(1, n + 1):
    for w in range(1, capacity + 1):
        if weights[i - 1] <= w:
            include_item = profits[i - 1] + dp[i - 1][w - weights[i - 1]]
            exclude_item = dp[i - 1][w]
            if include_item > exclude_item:
                dp[i][w] = include_item
            else:
                dp[i][w] = exclude_item
        else:
            dp[i][w] = dp[i - 1][w]

print("DP table:")
for row in dp:
    print(row)

print("\nMaximum profit:", dp[n][capacity])
