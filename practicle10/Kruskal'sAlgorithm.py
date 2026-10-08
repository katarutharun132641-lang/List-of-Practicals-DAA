# Time Complexity:
# Best Case    : O(E log E)
# Average Case : O(E log E)
# Worst Case   : O(E log E)
#
# Space Complexity:
# O(V)
#
# Where:
# V = Number of Vertices
# E = Number of Edges
#
# Note:
# Finds the Minimum Spanning Tree (MST)
# using Greedy Approach.
# =========================================================

# Edge class
class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


# Find Parent
def find(parent, x):
    while parent[x] != x:
        x = parent[x]
    return x


# Union of Sets
def union(parent, a, b):
    parent[a] = b


# Sort Edges by Weight
def sort_edges(edges):
    edges.sort(key=lambda edge: edge.w)
