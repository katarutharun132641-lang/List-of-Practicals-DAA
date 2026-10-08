# Time Complexity:
# Best Case    : O(V + E)
# Average Case : O(V + E)
# Worst Case   : O(V + E)
#
# Space Complexity:
# O(V)
#
# Where:
# V = Number of Vertices
# E = Number of Edges
# =========================================================
def dfs(graph, visited, v, n):
    visited[v] = True
    print(v, end=" ")

    for i in range(n):
        if graph[v][i] == 1 and not visited[i]:
            dfs(graph, visited, i, n)



