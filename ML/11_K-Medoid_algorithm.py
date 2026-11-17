"""K-Medoids clustering; each cluster center is an actual observation."""
import math
import random


def distance(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def k_medoids(points, k, iterations=100, seed=1):
    if not points or not 1 <= k <= len(points):
        raise ValueError("k must be between 1 and the number of points.")
    rng = random.Random(seed)
    medoid_indices = rng.sample(range(len(points)), k)
    for _ in range(iterations):
        assignments = [min(range(k), key=lambda c: distance(point, points[medoid_indices[c]]))
                       for point in points]
        changed = False
        for cluster in range(k):
            members = [i for i, assignment in enumerate(assignments) if assignment == cluster]
            if not members:
                continue
            candidate = min(members, key=lambda i: sum(distance(points[i], points[j]) for j in members))
            if candidate != medoid_indices[cluster]:
                medoid_indices[cluster], changed = candidate, True
        if not changed:
            break
    assignments = [min(range(k), key=lambda c: distance(point, points[medoid_indices[c]]))
                   for point in points]
    return assignments, [points[i] for i in medoid_indices]


if __name__ == "__main__":
    points = [[1, 1], [1, 2], [2, 1], [8, 8], [9, 8], [8, 9]]
    assignments, medoids = k_medoids(points, 2)
    print("Cluster assignments:", assignments)
    print("Medoids (actual points):", medoids)
