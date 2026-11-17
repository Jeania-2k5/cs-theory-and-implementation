"""Multiple linear regression solved with normal equations and Gaussian elimination."""


def solve_linear_system(matrix, values):
    n = len(values)
    augmented = [row[:] + [values[i]] for i, row in enumerate(matrix)]
    for column in range(n):
        pivot = max(range(column, n), key=lambda row: abs(augmented[row][column]))
        if abs(augmented[pivot][column]) < 1e-12:
            raise ValueError("The regression features are linearly dependent.")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        divisor = augmented[column][column]
        augmented[column] = [value / divisor for value in augmented[column]]
        for row in range(n):
            if row != column:
                factor = augmented[row][column]
                augmented[row] = [a - factor * b for a, b in zip(augmented[row], augmented[column])]
    return [augmented[i][-1] for i in range(n)]


def fit_regression(X, y):
    if not X or len(X) != len(y):
        raise ValueError("Training data must be non-empty and equally sized.")
    design = [[1.0] + row for row in X]
    columns = len(design[0])
    gram = [[sum(row[i] * row[j] for row in design) for j in range(columns)]
            for i in range(columns)]
    target = [sum(row[i] * value for row, value in zip(design, y)) for i in range(columns)]
    return solve_linear_system(gram, target)


def predict(row, coefficients):
    return coefficients[0] + sum(value * coefficient for value, coefficient in zip(row, coefficients[1:]))


if __name__ == "__main__":
    X = [[1, 1], [2, 1], [3, 2], [4, 3], [5, 3]]
    y = [4, 7, 10, 14, 17]
    coefficients = fit_regression(X, y)
    print("Coefficients (intercept first):", [round(c, 3) for c in coefficients])
    print("Prediction for [6, 4]:", round(predict([6, 4], coefficients), 3))
