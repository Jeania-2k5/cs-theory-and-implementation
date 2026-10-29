# Program for Jacobi Iteration Method
# Simplest beginner-friendly version with predefined values.

print("Jacobi Iteration Method")
print("-" * 60)

# Sample linear system:
# 10x -  y + 2z =   6
# - x + 11y - z =  22
# 2x -  y + 10z = -10
a = [
    [10.0, -1.0, 2.0],
    [-1.0, 11.0, -1.0],
    [2.0, -1.0, 10.0],
]
b = [6.0, 22.0, -10.0]

x1_old = 0.0
x2_old = 0.0
x3_old = 0.0

tolerance = 0.00001
max_iterations = 25

print("Iter\t x1\t\t x2\t\t x3\t\t Error")

for i in range(1, max_iterations + 1):
    x1 = (b[0] - a[0][1] * x2_old - a[0][2] * x3_old) / a[0][0]
    x2 = (b[1] - a[1][0] * x1_old - a[1][2] * x3_old) / a[1][1]
    x3 = (b[2] - a[2][0] * x1_old - a[2][1] * x2_old) / a[2][2]

    e1 = abs(x1 - x1_old)
    e2 = abs(x2 - x2_old)
    e3 = abs(x3 - x3_old)
    error = max(e1, e2, e3)

    print(i, "\t", round(x1, 6), "\t", round(x2, 6), "\t", round(x3, 6), "\t", round(error, 6))

    if error < tolerance:
        print("\nFinal Solution:")
        print("x1 =", x1)
        print("x2 =", x2)
        print("x3 =", x3)
        break

    x1_old = x1
    x2_old = x2
    x3_old = x3
