array = [8, 3, 5, 4, 7, 6, 2]
print("Unsorted list: " + ' '.join(map(str, array)))

n = len(array)

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if array[j] < array[min_index]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i]
    if i == 0:
        print("List after first iteration: " + ' '.join(map(str, array)))

print("Sorted list: " + ' '.join(map(str, array)))
