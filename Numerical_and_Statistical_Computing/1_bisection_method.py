# Program for Bisection Method
# Simplest beginner-friendly version with predefined values.


def f(x):
    # Sample equation: f(x) = x^3 - x - 2
    return x**3 - x - 2


# Fixed starting interval [a, b]
a = 1.0
b = 2.0

# Accuracy and maximum loop count
tolerance = 0.00001
max_iterations = 50

fa = f(a)
fb = f(b)

print("Bisection Method")
print("f(x) = x^3 - x - 2")
print("a =", a, ", b =", b)
print("Tolerance =", tolerance)
print("-" * 60)

# Bisection works only if f(a) and f(b) have opposite signs
if fa * fb > 0:
    print("Invalid interval. Choose a and b such that f(a)*f(b) < 0")
else:
    print("Iter\t   a\t\t   b\t\t   c\t\t  Error")

    previous_c = 0.0

    for i in range(1, max_iterations + 1):
        # Midpoint of current interval
        c = (a + b) / 2.0

        # Error in current iteration
        if i == 1:
            error = 0.0
        else:
            error = abs(c - previous_c)

        print(i, "\t", round(a, 6), "\t", round(b, 6), "\t", round(c, 6), "\t", round(error, 6))

        # Stop if required accuracy is reached
        if i > 1 and error < tolerance:
            print("\nApproximate root =", c)
            break

        # Keep the half interval where sign change exists
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        previous_c = c
