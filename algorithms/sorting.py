

"""Bubble Sort"""

def bubble_sort(arr):
    result = arr.copy()
    n = len(result)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n -i-1):
            if result[j] > result[j + 1]:
                result[j], result[j+1] = result[j+1], result[j]
                swapped = True
                
        if not swapped:
            break
    return result

"""Selection Sort"""

def selection_sort(arr):
    result = arr.copy()
    n = len(result)
    
    for i in range(n):
        min_index = i
        
        for j in range(i + 1,n):
            if result[j] < result[min_index]:
                min_index = j
                
        result[i], result[min_index] = result[min_index], result[i]
        
    return result

"""Insertion sort"""
 
def insertion_sort(arr):
    result = arr.copy()
    
    for i in range(1,len(result)):
        key = result[i]
        j = i - 1      # previous = j
        
        while j >= 0 and result[j] > key:
            result[j + 1]  = result[j]
            j -= 1
            
        result[j + 1] = key
        
    return result

"""Merge Sort"""
def merge_sort(arr):
    
    if len(arr) <= 1:
        return arr.copy()
    
    mid = len(arr) // 2
    
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    result = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

"""Quick Sort"""

def quick_sort(arr):
    result = arr.copy()
    _quick_sort(result, 0, len(result) - 1)
    return result

def _quick_sort(arr,low,high):
    
    if low < high:
        pivot_index = _partition(arr,low,high)
        _quick_sort(arr, low, pivot_index - 1)
        _quick_sort(arr, pivot_index + 1, high)
        
def _partition(arr, low, high):

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


