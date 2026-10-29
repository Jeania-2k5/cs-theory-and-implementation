# Program for Newton-Raphson Method
# Simplest beginner-friendly version with predefined values.


def f(x):
    # Sample equation: f(x) = x^3 - x - 2
    return x**3 - x - 2


def df(x):
    # Derivative: f'(x) = 3x^2 - 1
    return 3 * x**2 - 1


x0 = 1.5
tolerance = 0.00001
max_iterations = 50

print("Newton-Raphson Method")
print("f(x) = x^3 - x - 2")
print("f'(x) = 3x^2 - 1")
print("Initial guess x0 =", x0)
print("Tolerance =", tolerance)
print("-" * 60)
print("Iter\t x_n\t\t x_(n+1)\t Error")

for i in range(1, max_iterations + 1):
    fx0 = f(x0)
    dfx0 = df(x0)

    if dfx0 == 0:
        print("Derivative is zero. Method stopped.")
        break

    x1 = x0 - fx0 / dfx0
    error = abs(x1 - x0)

    print(i, "\t", round(x0, 6), "\t", round(x1, 6), "\t", round(error, 6))

    if error < tolerance:
        print("\nApproximate root =", x1)
        break

    x0 = x1
