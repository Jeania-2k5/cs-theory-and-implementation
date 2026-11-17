"""Agglomerative hierarchical clustering with single-linkage distance."""
import math


def point_distance(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def hierarchical_clustering(points, desired_clusters):
    if not points or not 1 <= desired_clusters <= len(points):
        raise ValueError("desired_clusters must be valid.")
    clusters = [[i] for i in range(len(points))]
    while len(clusters) > desired_clusters:
        pair = min(((i, j) for i in range(len(clusters)) for j in range(i + 1, len(clusters))),
                   key=lambda p: min(point_distance(points[a], points[b])
                                     for a in clusters[p[0]] for b in clusters[p[1]]))
        i, j = pair
        clusters[i].extend(clusters.pop(j))
    return clusters


if __name__ == "__main__":
    points = [[1, 1], [1, 2], [2, 1], [8, 8], [9, 8], [8, 9]]
    print("Single-linkage clusters:", hierarchical_clustering(points, 2))
