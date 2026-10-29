# 3) Quick Sort (Non-Linear Time Sorting)

arr = [10, 7, 8, 9, 1, 5]

print("Original array:", arr)


def partition(a, low, high):
    pivot = a[high]
    i = low - 1

    for j in range(low, high):
        if a[j] <= pivot:
            i = i + 1
            a[i], a[j] = a[j], a[i]

    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1


def quick_sort(a, low, high):
    if low < high:
        pi = partition(a, low, high)
        print("Pivot placed at index", pi, "->", a)
        quick_sort(a, low, pi - 1)
        quick_sort(a, pi + 1, high)


quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
