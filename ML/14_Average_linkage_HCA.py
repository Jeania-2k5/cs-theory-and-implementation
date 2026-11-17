"""Agglomerative hierarchical clustering with average-linkage distance."""
import math


def distance(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def average_linkage(points, desired_clusters):
    if not points or not 1 <= desired_clusters <= len(points):
        raise ValueError("desired_clusters must be valid.")
    clusters = [[i] for i in range(len(points))]
    while len(clusters) > desired_clusters:
        def cluster_distance(pair):
            left, right = clusters[pair[0]], clusters[pair[1]]
            distances = [distance(points[x], points[y]) for x in left for y in right]
            return sum(distances) / len(distances)
        i, j = min(((a, b) for a in range(len(clusters)) for b in range(a + 1, len(clusters))),
                   key=cluster_distance)
        clusters[i].extend(clusters.pop(j))
    return clusters


if __name__ == "__main__":
    points = [[1, 1], [1, 2], [2, 1], [8, 8], [9, 8], [8, 9]]
    print("Average-linkage clusters:", average_linkage(points, 2))
