# Bubble Sort
# Time Complexity:
# Best Case    : O(n)
# Average Case : O(n^2)
# Worst Case   : O(n^2)
#
# Space Complexity:
# O(1)
# =========================================================
def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
