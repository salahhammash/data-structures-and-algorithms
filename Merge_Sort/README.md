# Insertion Sort

> create a method that sorts a function based on the input array

# Approach & Efficiency

> Time ==> O(n log n)

> space ==> O(n)

## Whiteboard Process
![merg_sort](./assest/merg%20sort.png)

# Solution 

   def mergeSort(arr):
    n = len(arr)
    
    if n > 1:
        mid = n//2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        merge(left, right, arr)
    return arr    
        
    
def merge(left, right, arr):
    i = 0
    j = 0
    k = 0
    
    while i < len(left) and j < len(right):
        if left[i]<= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
        k =k + 1

    if i == len(left):
        arr[k:] = right[j:]
    else :
        arr[k:] = left[i:]
        
    