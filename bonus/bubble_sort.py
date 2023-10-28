array = [8, 3, 5, 4, 7, 6, 2]
print("Unsorted list: " + ' '.join(map(str, array)))

n = len(array)

for i in range(n - 1):
    for j in range (0, n - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
    if i == 0:
        print("List after first iteration: " + ' '.join(map(str, array)))

print("Sorted list: " + ' '.join(map(str, array)))
