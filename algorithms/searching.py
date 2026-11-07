
"""Linear Search"""
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1

"""Binary Search"""
def binary_search(arr,target):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            start = mid + 1
        
        else:
            end = mid - 1
    
    return - 1
        
