arr = [45, 6, 33, 12, 9, 3, 2, 1, 0]
print(arr)


def sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


print(f"Sorted array: {sort(arr)}")
