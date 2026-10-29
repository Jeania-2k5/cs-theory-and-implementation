# Program for Gauss Elimination Method
# Simplest beginner-friendly version with predefined values.

print("Gauss Elimination Method")
print("-" * 60)

# Sample augmented matrix [A|B]
a = [
    [2.0, 1.0, -1.0, 8.0],
    [-3.0, -1.0, 2.0, -11.0],
    [-2.0, 1.0, 2.0, -3.0],
]
n = 3

print("Initial augmented matrix:")
for row in a:
    print(row)

# Forward elimination
valid = True
for i in range(n):
    if a[i][i] == 0:
        valid = False
        print("Zero pivot found. Method stopped.")
        break

    for j in range(i + 1, n):
        factor = a[j][i] / a[i][i]
        for k in range(i, n + 1):
            a[j][k] = a[j][k] - factor * a[i][k]

    print("\nAfter eliminating column", i + 1)
    for row in a:
        print([round(value, 6) for value in row])

if valid:
    # Back substitution
    x = [0.0, 0.0, 0.0]

    x[2] = a[2][3] / a[2][2]
    x[1] = (a[1][3] - a[1][2] * x[2]) / a[1][1]
    x[0] = (a[0][3] - a[0][2] * x[2] - a[0][1] * x[1]) / a[0][0]

    print("\nFinal Solution:")
    print("x1 =", x[0])
    print("x2 =", x[1])
    print("x3 =", x[2])
