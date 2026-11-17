"""Simple linear regression: y = slope*x + intercept."""


def fit_line(x_values, y_values):
    if len(x_values) != len(y_values) or len(x_values) < 2:
        raise ValueError("Need at least two equally sized lists.")
    x_mean, y_mean = sum(x_values) / len(x_values), sum(y_values) / len(y_values)
    denominator = sum((x - x_mean) ** 2 for x in x_values)
    if denominator == 0:
        raise ValueError("x values must not all be identical.")
    slope = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_values, y_values)) / denominator
    return slope, y_mean - slope * x_mean


def predict(x, parameters):
    slope, intercept = parameters
    return slope * x + intercept


def mean_squared_error(actual, predicted):
    return sum((a - p) ** 2 for a, p in zip(actual, predicted)) / len(actual)


if __name__ == "__main__":
    x, y = [1, 2, 3, 4, 5], [2, 4, 5, 8, 10]
    model = fit_line(x, y)
    predictions = [predict(value, model) for value in x]
    print("Slope:", round(model[0], 3), "Intercept:", round(model[1], 3))
    print("Predicted y for x=6:", round(predict(6, model), 3))
    print("Mean squared error:", round(mean_squared_error(y, predictions), 3))
