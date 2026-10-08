# Iterative Factorial
#
# Time Complexity:
# Best Case    : O(n)
# Average Case : O(n)
# Worst Case   : O(n)
#
# Space Complexity:
# O(1)
# =========================================================
def iterative_factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact
