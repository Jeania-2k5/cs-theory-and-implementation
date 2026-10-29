# Program for Newton Backward Interpolation Method
# This program calculates interpolated value using Newton Backward formula.

print("Newton Backward Interpolation Method")
print("-" * 60)

x = [1891.0, 1901.0, 1911.0, 1921.0, 1931.0]
y = [46.0, 66.0, 81.0, 93.0, 101.0]
xp = 1925.0
n = len(x)

print("x values:", x)
print("y values:", y)
print("Interpolation point xp =", xp)

h = x[1] - x[0]

# Difference table
d = [[0.0 for j in range(n)] for i in range(n)]
for i in range(n):
    d[i][0] = y[i]

for j in range(1, n):
    for i in range(n - j):
        d[i][j] = d[i + 1][j - 1] - d[i][j - 1]

print("\nDifference Table:")
for i in range(n):
    print([round(d[i][j], 6) for j in range(n - i)])

u = (xp - x[n - 1]) / h

yp = d[n - 1][0]
u_term = 1.0
fact = 1

for k in range(1, n):
    u_term = u_term * (u + (k - 1))
    fact = fact * k
    yp = yp + (u_term * d[n - 1 - k][k]) / fact

print("\nInterpolated value at", xp, "=", yp)
