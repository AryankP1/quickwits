def knapsack(w, v, f):
    n = len(f)
    dp = [[0] * (w + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight, volume, value = f[i - 1]
        for j in range(1, w + 1):
            if weight <= j:
                dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][w]

# Example usage
w = 100
v = 150
f = [[60, 70, 60], [30, 80, 40], [35, 70, 70]]
max_value = knapsack(w, v, f)
print("Maximum value:", max_value)
