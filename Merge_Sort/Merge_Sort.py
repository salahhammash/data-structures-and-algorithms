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
     # we used recurgen    
        
    
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
        
        
# print(mergeSort([8,4,23,42,16,15]))