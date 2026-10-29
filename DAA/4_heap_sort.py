# 4) Heap Sort (Non-Linear Time Sorting)

arr = [12, 11, 13, 5, 6, 7]

print("Original array:", arr)


def heapify(a, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and a[left] > a[largest]:
        largest = left

    if right < n and a[right] > a[largest]:
        largest = right

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)


n = len(arr)

# Build max heap
for i in range(n // 2 - 1, -1, -1):
    heapify(arr, n, i)

print("Max heap formed:", arr)

# Extract elements one by one
for i in range(n - 1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    heapify(arr, i, 0)
    print("Step:", arr)

print("Sorted array:", arr)
