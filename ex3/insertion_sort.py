array = [12, 11, 13, 5, 6, 7]
print("Original array:", array)

for i in range(1, len(array)):
    key = array[i]
    j = i - 1

    print(f"Iteration {i}: {array[:i]} (sorted) + {array[i:]} (unsorted)")

    while j >= 0 and key < array[j]:
        array[j + 1] = array[j]
        j -= 1

    array[j + 1] = key

print("Sorted array:", array)
