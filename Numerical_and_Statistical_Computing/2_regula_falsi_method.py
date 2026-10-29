# Program for Regula Falsi Method
# Simplest beginner-friendly version with predefined values.


def f(x):
    # Sample equation: f(x) = x^3 - x - 2
    return x**3 - x - 2


a = 1.0
b = 2.0
tolerance = 0.00001
max_iterations = 50

fa = f(a)
fb = f(b)

print("Regula Falsi Method")
print("f(x) = x^3 - x - 2")
print("a =", a, ", b =", b)
print("Tolerance =", tolerance)
print("-" * 60)

if fa * fb > 0:
    print("Invalid interval. Choose a and b such that f(a)*f(b) < 0")
else:
    print("Iter\t   a\t\t   b\t\t   x\t\t  Error")

    previous_x = 0.0

    for i in range(1, max_iterations + 1):
        denominator = fb - fa
        if denominator == 0:
            print("Division by zero. Method stopped.")
            break

        x = (a * fb - b * fa) / denominator
        fx = f(x)

        if i == 1:
            error = 0.0
        else:
            error = abs(x - previous_x)

        print(i, "\t", round(a, 6), "\t", round(b, 6), "\t", round(x, 6), "\t", round(error, 6))

        if i > 1 and error < tolerance:
            print("\nApproximate root =", x)
            break

        if fa * fx < 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx

        previous_x = x
