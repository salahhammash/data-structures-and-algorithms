# Insertion Sort

> create a method that sorts a function based on the input array

# Approach & Efficiency

> Time ==> O(n^2)

> space ==> O(n)

# Solution 

    def insert (sorted,value):
  
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
  
    sorted =[]
    sorted.append(input[0])
    # or sorted=[0]
    # sorted[0] = input[0]
    for i in range(1 , len(input)):
        insert(sorted, input[i])
    return sorted
    