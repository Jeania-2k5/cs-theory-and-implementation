"""Random Forest classifier using bootstrap samples and hand-built trees."""
import math
import random
from collections import Counter


def entropy(labels):
    counts = Counter(labels)
    return -sum((n / len(labels)) * math.log2(n / len(labels)) for n in counts.values())


def majority(labels):
    return Counter(labels).most_common(1)[0][0]


def best_split(X, y, candidates):
    base = entropy(y)
    best = None
    for feature in candidates:
        for threshold in sorted({row[feature] for row in X}):
            left = [i for i, row in enumerate(X) if row[feature] <= threshold]
            right = [i for i, row in enumerate(X) if row[feature] > threshold]
            if not left or not right:
                continue
            gain = base - (len(left) * entropy([y[i] for i in left]) +
                           len(right) * entropy([y[i] for i in right])) / len(y)
            if best is None or gain > best[0]:
                best = gain, feature, threshold, left, right
    return best


def build_tree(X, y, features, depth, max_depth):
    node = {"prediction": majority(y)}
    if len(set(y)) == 1 or depth >= max_depth:
        return node
    split = best_split(X, y, features)
    if split is None or split[0] <= 0:
        return node
    _, feature, threshold, left, right = split
    node.update(feature=feature, threshold=threshold,
                left=build_tree([X[i] for i in left], [y[i] for i in left],
                                features, depth + 1, max_depth),
                right=build_tree([X[i] for i in right], [y[i] for i in right],
                                 features, depth + 1, max_depth))
    return node


def tree_predict(tree, row):
    if "feature" not in tree:
        return tree["prediction"]
    side = "left" if row[tree["feature"]] <= tree["threshold"] else "right"
    return tree_predict(tree[side], row)


class RandomForest:
    def __init__(self, tree_count=7, max_depth=4, feature_fraction=0.7, seed=7):
        self.tree_count, self.max_depth = tree_count, max_depth
        self.feature_fraction, self.random = feature_fraction, random.Random(seed)
        self.trees = []

    def fit(self, X, y):
        if not X or len(X) != len(y):
            raise ValueError("Training data must be non-empty and equally sized.")
        feature_count = len(X[0])
        choose = max(1, round(feature_count * self.feature_fraction))
        self.trees = []
        for _ in range(self.tree_count):
            sample_indices = [self.random.randrange(len(X)) for _ in X]
            features = self.random.sample(range(feature_count), choose)
            sample_X = [X[i] for i in sample_indices]
            sample_y = [y[i] for i in sample_indices]
            self.trees.append(build_tree(sample_X, sample_y, features, 0, self.max_depth))

    def predict(self, row):
        if not self.trees:
            raise ValueError("Call fit before predict.")
        votes = [tree_predict(tree, row) for tree in self.trees]
        return Counter(votes).most_common(1)[0][0], votes


if __name__ == "__main__":
    X = [[1, 1], [2, 1], [1, 2], [7, 7], [8, 7], [7, 8]]
    y = ["small", "small", "small", "large", "large", "large"]
    forest = RandomForest()
    forest.fit(X, y)
    print("Random Forest prediction:", forest.predict([6, 7]))
