 """K-Nearest Neighbors classification implemented from scratch.

KNN stores the training examples, measures their distance from a new point,
and predicts the majority class among the k closest examples.
"""
import math
from collections import Counter


def euclidean_distance(first, second):
    if len(first) != len(second):
        raise ValueError("Both points must have the same number of features.")
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(first, second)))


def predict_knn(features, labels, new_point, k=3):
    if len(features) != len(labels) or not features:
        raise ValueError("Features and labels must be non-empty and equally sized.")
    if not 1 <= k <= len(features):
        raise ValueError("k must be between 1 and the number of training examples.")
    ranked = [(euclidean_distance(row, new_point), label)
              for row, label in zip(features, labels)]
    ranked.sort(key=lambda item: item[0])
    nearest_labels = [label for _, label in ranked[:k]]
    return Counter(nearest_labels).most_common(1)[0][0], ranked[:k]


if __name__ == "__main__":
    X = [[2, 60], [3, 65], [4, 70], [6, 80], [7, 85], [8, 90]]
    y = ["Fail", "Fail", "Fail", "Pass", "Pass", "Pass"]
    point = [5, 80]
    prediction, neighbors = predict_knn(X, y, point, k=3)
    print("KNN classification")
    print("Nearest neighbors:", neighbors)
    print("Prediction for", point, ":", prediction)
