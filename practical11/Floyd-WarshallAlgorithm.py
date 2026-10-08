# Time Complexity:
# Best Case    : O(V^3)
# Average Case : O(V^3)
# Worst Case   : O(V^3)
#
# Space Complexity:
# O(V^2)
#
# Where:
# V = Number of Vertices
#
# Note:
# Finds the shortest paths between all pairs
# of vertices in a weighted graph.
# =========================================================

INF = 9999


def floyd_warshall(graph, n):
    # Floyd-Warshall Algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

