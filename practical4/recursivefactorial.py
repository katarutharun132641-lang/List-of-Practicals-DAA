# Recursive Factorial
#
# Time Complexity:
# Best Case    : O(n)
# Average Case : O(n)
# Worst Case   : O(n)
#
# Space Complexity:
# O(n)
#
# Note:
# Recursive method uses the function call stack.
# =========================================================
def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * recursive_factorial(n - 1)
