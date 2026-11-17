"""Binary logistic regression trained by gradient descent."""
import math


def sigmoid(value):
    value = max(-500, min(500, value))
    return 1 / (1 + math.exp(-value))


class LogisticRegression:
    def __init__(self, learning_rate=0.1, epochs=3000):
        self.learning_rate, self.epochs = learning_rate, epochs
        self.weights, self.bias = [], 0.0

    def fit(self, X, y):
        if not X or len(X) != len(y) or any(label not in (0, 1) for label in y):
            raise ValueError("Use non-empty, equally sized data with labels 0 or 1.")
        self.weights = [0.0] * len(X[0])
        self.bias = 0.0
        for _ in range(self.epochs):
            gradients = [0.0] * len(self.weights)
            bias_gradient = 0.0
            for row, target in zip(X, y):
                probability = sigmoid(sum(w * x for w, x in zip(self.weights, row)) + self.bias)
                error = probability - target
                gradients = [g + error * x for g, x in zip(gradients, row)]
                bias_gradient += error
            scale = 1 / len(X)
            self.weights = [w - self.learning_rate * g * scale
                            for w, g in zip(self.weights, gradients)]
            self.bias -= self.learning_rate * bias_gradient * scale

    def probability(self, row):
        return sigmoid(sum(w * x for w, x in zip(self.weights, row)) + self.bias)

    def predict(self, row):
        return int(self.probability(row) >= 0.5)


if __name__ == "__main__":
    X = [[1, 1], [1, 2], [2, 1], [6, 6], [7, 6], [6, 7]]
    y = [0, 0, 0, 1, 1, 1]
    model = LogisticRegression()
    model.fit(X, y)
    print("Weights:", [round(w, 3) for w in model.weights], "Bias:", round(model.bias, 3))
    print("Predictions:", [model.predict(row) for row in [[2, 2], [7, 7]]])
