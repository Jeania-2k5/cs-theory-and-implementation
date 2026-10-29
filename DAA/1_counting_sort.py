# 1) Counting Sort (Linear Time Sorting)

arr = [4, 2, 2, 8, 3, 3, 1]

print("Original array:", arr)

# Find maximum value to create count array
max_value = max(arr)
count = [0] * (max_value + 1)

# Count frequency of each number
for num in arr:
    count[num] = count[num] + 1

print("Count array after frequency count:", count)

# Build sorted array
sorted_arr = []
for i in range(len(count)):
    while count[i] > 0:
        sorted_arr.append(i)
        count[i] = count[i] - 1

print("Sorted array:", sorted_arr)
