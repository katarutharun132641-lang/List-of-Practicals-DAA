# Time Complexity:
# Best Case    : O(n * Amount)
# Average Case : O(n * Amount)
# Worst Case   : O(n * Amount)
#
# Space Complexity:
# O(Amount)
#
# Where:
# n = Number of coin denominations
# Amount = Total amount to make
#
# Note:
# Finds the minimum number of coins required
# to make the given amount.
# =========================================================

INF = float('inf')


def coin_change(coins, n, amount):
    # Initialize DP array
    dp = [INF] * (amount + 1)
    dp[0] = 0

    # Fill DP table
    for i in range(1, amount + 1):
        for j in range(n):
            if coins[j] <= i:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)

    if dp[amount] == INF:
        return -1

    return dp[amount]
