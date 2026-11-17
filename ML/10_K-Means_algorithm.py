"""K-Means clustering with iterative assignment and centroid updates."""
import math
import random


def distance(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def kmeans(points, k, iterations=100, seed=1):
    if not points or not 1 <= k <= len(points):
        raise ValueError("k must be between 1 and the number of points.")
    randomizer = random.Random(seed)
    centroids = [list(point) for point in randomizer.sample(points, k)]
    for _ in range(iterations):
        assignments = [min(range(k), key=lambda c: distance(point, centroids[c]))
                       for point in points]
        updated = []
        for cluster in range(k):
            members = [point for point, assignment in zip(points, assignments)
                       if assignment == cluster]
            updated.append([sum(point[i] for point in members) / len(members)
                            for i in range(len(points[0]))] if members else centroids[cluster])
        if updated == centroids:
            break
        centroids = updated
    return assignments, centroids


if __name__ == "__main__":
    points = [[1, 1], [1, 2], [2, 1], [8, 8], [9, 8], [8, 9]]
    assignments, centroids = kmeans(points, 2)
    print("Cluster assignments:", assignments)
    print("Centroids:", centroids)
