def quicksort(array, left, right):
    if left < right:
        index = partition(array, left, right)
        quicksort(array, left, index - 1)
        quicksort(array, index, right)


def partition(array, left, right):
    pivot_index = left
    pivot = array[pivot_index]

    while left <= right:
        while array[left] < pivot:
            left += 1

        while array[right] > pivot:
            right -= 1

        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    return left

array = [15, 7, 22, 9, 36, 2, 42, 18]
k = 4

def find_kth_element(array, k):
    temp_arr = array[:]
    quicksort(temp_arr, 0, len(temp_arr) - 1)
    return temp_arr[len(array) - k], array.index(temp_arr[-k])

print(find_kth_element(array, k))