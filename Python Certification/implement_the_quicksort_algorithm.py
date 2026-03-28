def quick_sort(arr):
    # Base case: empty or single element list
    if len(arr) <= 1:
        return arr[:]
    
    # Choose pivot (last element)
    pivot = arr[-1]
    
    # Partition into three lists
    less = []
    equal = []
    greater = []
    
    for num in arr:
        if num < pivot:
            less.append(num)
        elif num > pivot:
            greater.append(num)
        else:
            equal.append(num)
    
    # Recursively sort and combine
    return quick_sort(less) + equal + quick_sort(greater)
