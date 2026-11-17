"""Agglomerative hierarchical clustering with complete-linkage distance."""
import math


def distance(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def complete_linkage(points, desired_clusters):
    if not points or not 1 <= desired_clusters <= len(points):
        raise ValueError("desired_clusters must be valid.")
    clusters = [[i] for i in range(len(points))]
    while len(clusters) > desired_clusters:
        i, j = min(((a, b) for a in range(len(clusters)) for b in range(a + 1, len(clusters))),
                   key=lambda pair: max(distance(points[x], points[y])
                                         for x in clusters[pair[0]] for y in clusters[pair[1]]))
        clusters[i].extend(clusters.pop(j))
    return clusters


if __name__ == "__main__":
    points = [[1, 1], [1, 2], [2, 1], [8, 8], [9, 8], [8, 9]]
    print("Complete-linkage clusters:", complete_linkage(points, 2))
