def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def print_heap(arr):
    n = len(arr)
    levels = 0
    while (1 << levels) - 1 < n:
        levels += 1
    max_width = 1 << (levels - 1)
    for i in range(levels):
        level_width = 1 << i
        start_index = (1 << i) - 1
        end_index = min(start_index + level_width, n)
        spacing = ' ' * (max_width // level_width // 2)
        print(spacing, end=' ')
        
        for j in range(start_index, end_index):
            print(f'{arr[j]:2}', end=spacing*2)
        print()

arr = [12, 11, 13, 5, 6, 7]
print("\nArray não ordenado é:", arr)
print("Heap inicial:")
print_heap(arr)
heap_sort(arr)
print("\nArray ordenado é:", arr)
print_heap(arr)