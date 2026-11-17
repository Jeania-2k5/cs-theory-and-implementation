"""Polynomial regression using manually generated powers and normal equations."""


def solve(matrix, values):
    n = len(values)
    a = [row[:] + [values[i]] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(a[r][col]))
        if abs(a[pivot][col]) < 1e-12:
            raise ValueError("Polynomial features are linearly dependent.")
        a[col], a[pivot] = a[pivot], a[col]
        divisor = a[col][col]
        a[col] = [v / divisor for v in a[col]]
        for row in range(n):
            if row != col:
                factor = a[row][col]
                a[row] = [u - factor * v for u, v in zip(a[row], a[col])]
    return [a[i][-1] for i in range(n)]


def fit_polynomial(x_values, y_values, degree):
    if len(x_values) != len(y_values) or len(x_values) <= degree:
        raise ValueError("Need more observations than the polynomial degree.")
    design = [[x ** power for power in range(degree + 1)] for x in x_values]
    size = degree + 1
    gram = [[sum(row[i] * row[j] for row in design) for j in range(size)]
            for i in range(size)]
    target = [sum(row[i] * y for row, y in zip(design, y_values)) for i in range(size)]
    return solve(gram, target)


def predict(x, coefficients):
    return sum(coefficient * x ** power for power, coefficient in enumerate(coefficients))


if __name__ == "__main__":
    x, y = [0, 1, 2, 3, 4], [1, 2, 5, 10, 17]
    coefficients = fit_polynomial(x, y, degree=2)
    print("Polynomial coefficients:", [round(c, 3) for c in coefficients])
    print("Prediction for x=5:", round(predict(5, coefficients), 3))
