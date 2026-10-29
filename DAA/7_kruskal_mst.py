# 7) Kruskal's Algorithm (Greedy - Minimum Spanning Tree)

vertices = 6

# Edge format: (u, v, weight)
edges = [
    (0, 1, 4),
    (0, 2, 4),
    (1, 2, 2),
    (1, 3, 5),
    (2, 3, 5),
    (2, 4, 11),
    (3, 4, 2),
    (3, 5, 1),
    (4, 5, 7),
]

print("Given edges (u, v, w):")
for e in edges:
    print(e)


def find(parent, x):
    while parent[x] != x:
        x = parent[x]
    return x


def union(parent, rank, x, y):
    rx = find(parent, x)
    ry = find(parent, y)

    if rank[rx] < rank[ry]:
        parent[rx] = ry
    elif rank[rx] > rank[ry]:
        parent[ry] = rx
    else:
        parent[ry] = rx
        rank[rx] = rank[rx] + 1


edges.sort(key=lambda x: x[2])

parent = []
rank = []
for i in range(vertices):
    parent.append(i)
    rank.append(0)

mst = []
total_cost = 0

for u, v, w in edges:
    if find(parent, u) != find(parent, v):
        mst.append((u, v, w))
        total_cost = total_cost + w
        union(parent, rank, u, v)
        print("Selected edge:", (u, v, w))

print("\nMinimum Spanning Tree edges:")
for e in mst:
    print(e)

print("Total MST cost:", total_cost)
