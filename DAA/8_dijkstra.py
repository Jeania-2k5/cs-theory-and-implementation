# 8) Dijkstra's Algorithm (Greedy)

# Graph as adjacency matrix (0 means no direct edge)
graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0],
]

source = 0
n = len(graph)

dist = [999999] * n
visited = [False] * n
dist[source] = 0

for _ in range(n):
    # Pick unvisited vertex with smallest distance
    min_dist = 999999
    u = -1
    for i in range(n):
        if visited[i] is False and dist[i] < min_dist:
            min_dist = dist[i]
            u = i

    if u == -1:
        break

    visited[u] = True
    print("Visited node:", u, "Current distances:", dist)

    # Update neighbors
    for v in range(n):
        if graph[u][v] > 0 and visited[v] is False:
            if dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

print("\nShortest distances from source node", source)
for i in range(n):
    print("To", i, "=", dist[i])
