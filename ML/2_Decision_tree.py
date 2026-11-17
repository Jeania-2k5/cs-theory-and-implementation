"""A small numeric Decision Tree classifier built without ML libraries."""
import math
from collections import Counter


def entropy(labels):
    counts = Counter(labels)
    total = len(labels)
    return -sum((count / total) * math.log2(count / total)
                for count in counts.values())


def information_gain(rows, labels, feature, threshold):
    left = [label for row, label in zip(rows, labels) if row[feature] <= threshold]
    right = [label for row, label in zip(rows, labels) if row[feature] > threshold]
    if not left or not right:
        return 0.0
    weighted = (len(left) * entropy(left) + len(right) * entropy(right)) / len(labels)
    return entropy(labels) - weighted


def majority(labels):
    return Counter(labels).most_common(1)[0][0]


def build_tree(rows, labels, depth=0, max_depth=3):
    node = {"prediction": majority(labels)}
    if len(set(labels)) == 1 or depth == max_depth:
        return node
    best = None
    for feature in range(len(rows[0])):
        for threshold in sorted({row[feature] for row in rows}):
            gain = information_gain(rows, labels, feature, threshold)
            if best is None or gain > best[0]:
                best = (gain, feature, threshold)
    if best is None or best[0] <= 0:
        return node
    _, feature, threshold = best
    left_rows = [row for row in rows if row[feature] <= threshold]
    right_rows = [row for row in rows if row[feature] > threshold]
    left_labels = [label for row, label in zip(rows, labels) if row[feature] <= threshold]
    right_labels = [label for row, label in zip(rows, labels) if row[feature] > threshold]
    node.update(feature=feature, threshold=threshold,
               left=build_tree(left_rows, left_labels, depth + 1, max_depth),
               right=build_tree(right_rows, right_labels, depth + 1, max_depth))
    return node


def predict(tree, row):
    if "feature" not in tree:
        return tree["prediction"]
    branch = tree["left"] if row[tree["feature"]] <= tree["threshold"] else tree["right"]
    return predict(branch, row)


if __name__ == "__main__":
    X = [[1, 1], [1, 2], [2, 1], [6, 6], [7, 6], [8, 7]]
    y = ["No", "No", "No", "Yes", "Yes", "Yes"]
    tree = build_tree(X, y)
    print("Decision tree predictions:", [predict(tree, row) for row in [[2, 2], [7, 7]]])
