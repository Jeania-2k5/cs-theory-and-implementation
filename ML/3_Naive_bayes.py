"""Categorical Naive Bayes classifier with Laplace smoothing."""
from collections import Counter


class NaiveBayes:
    def __init__(self):
        self.classes = []
        self.priors = {}
        self.counts = {}
        self.feature_values = []

    def fit(self, X, y):
        if not X or len(X) != len(y):
            raise ValueError("Training data must be non-empty and equally sized.")
        self.classes = sorted(set(y))
        self.feature_values = [set(row[i] for row in X) for i in range(len(X[0]))]
        class_counts = Counter(y)
        total = len(y)
        self.priors = {c: class_counts[c] / total for c in self.classes}
        self.counts = {c: [Counter() for _ in self.feature_values] for c in self.classes}
        for row, label in zip(X, y):
            for i, value in enumerate(row):
                self.counts[label][i][value] += 1

    def predict(self, row):
        if not self.classes:
            raise ValueError("Call fit before predict.")
        scores = {}
        for label in self.classes:
            log_probability = self._log(self.priors[label])
            class_total = sum(self.counts[label][0].values())
            for i, value in enumerate(row):
                numerator = self.counts[label][i][value] + 1
                denominator = class_total + len(self.feature_values[i])
                log_probability += self._log(numerator / denominator)
            scores[label] = log_probability
        return max(scores, key=scores.get), scores

    @staticmethod
    def _log(value):
        import math
        return math.log(value)


if __name__ == "__main__":
    X = [["Sunny", "Hot"], ["Sunny", "Cool"], ["Rain", "Cool"],
         ["Rain", "Mild"], ["Cloudy", "Mild"], ["Cloudy", "Cool"]]
    y = ["No", "No", "Yes", "Yes", "Yes", "Yes"]
    model = NaiveBayes()
    model.fit(X, y)
    prediction, scores = model.predict(["Sunny", "Mild"])
    print("Naive Bayes prediction:", prediction)
    print("Log posterior scores:", scores)
