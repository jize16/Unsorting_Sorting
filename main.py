full_name = "Jizea Tradio"


def create_array(name):
    """Make an array of letters: no symbols or spaces, no duplicate letters."""
    array = []
    for ch in name.upper():
        if ch.isalpha() and ch not in array:
            array.append(ch)
    return array


def bubble_sort(arr):
    """Bubble Sort: compare adjacent elements and swap if in the wrong order."""
    arr = arr[:]  # copy, so the unsorted array stays unchanged
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


unsorted_array = create_array(full_name)
sorted_array = bubble_sort(unsorted_array)

print("Full Name:      ", full_name)
print("Unsorted array: ", unsorted_array)
print("Sorted array:   ", sorted_array)