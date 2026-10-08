# Time Complexity:
# Best Case    : O(n!)
# Average Case : O(n!)
# Worst Case   : O(n!)
#
# Space Complexity:
# O(n)
#
# Where:
# n = Number of Cities
#
# Note:
# Uses Backtracking to find the minimum cost
# Hamiltonian Cycle.
# =========================================================

INF = float('inf')


# Recursive Function
def tsp(graph, visited, city, count, cost, n):
    global min_cost

    # All cities visited
    if count == n and graph[city][0] != 0:
        cost += graph[city][0]
        min_cost = min(min_cost, cost)
        return

    for i in range(n):
        if not visited[i] and graph[city][i] != 0:
            visited[i] = True

            tsp(graph, visited, i, count + 1, cost + graph[city][i], n)

            visited[i] = False
