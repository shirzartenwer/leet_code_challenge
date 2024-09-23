def quick_sort(array: list):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        # When comparing with the rest of the array, it must start at array[1:] in this case, to exclude the pivot
        less = [i for i in array[1:] if i < pivot]
        more = [i for i in array[1:] if i >= pivot]
        return quick_sort(less) + [pivot] + quick_sort(more)


result = quick_sort([5, 10, 3, 9, 8, 25, 29, 3])
print("sorted array is:", result)
