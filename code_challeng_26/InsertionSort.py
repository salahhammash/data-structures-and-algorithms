def insert (sorted,value):
    """
    Inserts a value into a sorted list in a correct position.

    Args:
        sorted_list (list): A sorted list of integers.
        value (int): The value to be inserted into the sorted list.

    Returns:
        None
    """
    i = 0
    while i < len(sorted) and value > sorted[i]:
        i+=1 
    while i < len(sorted):
        temp = sorted[i]
        sorted[i] = value
        value = temp
        i+=1
    sorted.append(value)
    

def insertionSort(input):
    """
    Sorts the input list using the insertion sort algorithm.

    Args:
        input_list (list): A list of integers to be sorted.

    Returns:
        list: A new list containing the sorted integers.
    """
    sorted =[]
    sorted.append(input[0])
    # or sorted=[0]
    # sorted[0] = input[0]
    for i in range(1 , len(input)):
        insert(sorted, input[i])
    return sorted
    
print(insertionSort([8,4,23,42,16,15]))    