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


# =========================================================
# Breadth First Search (BFS)
#
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
def bfs(graph, visited, start, n):
    queue = deque()

    visited[start] = True
    queue.append(start)

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in range(n):
            if graph[v][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)
