# 2) Radix Sort (Linear Time Sorting)

arr = [170, 45, 75, 90, 802, 24, 2, 66]

print("Original array:", arr)


def counting_sort_by_digit(a, exp):
    n = len(a)
    output = [0] * n
    count = [0] * 10

    # Count digits at current place value
    for i in range(n):
        digit = (a[i] // exp) % 10
        count[digit] = count[digit] + 1

    # Prefix sum for positions
    for i in range(1, 10):
        count[i] = count[i] + count[i - 1]

    # Build output from right to left for stability
    i = n - 1
    while i >= 0:
        digit = (a[i] // exp) % 10
        output[count[digit] - 1] = a[i]
        count[digit] = count[digit] - 1
        i = i - 1

    # Copy output back to original array
    for i in range(n):
        a[i] = output[i]


max_value = max(arr)
exp = 1

# Sort by 1s, 10s, 100s, ...
while max_value // exp > 0:
    counting_sort_by_digit(arr, exp)
    print("After sorting with exp =", exp, ":", arr)
    exp = exp * 10

print("Sorted array:", arr)
