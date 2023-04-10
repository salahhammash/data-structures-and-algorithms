# code chaleng 1 (reverse)
<!-- Description of the challenge -->
we need a function which takes in an array and a value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.


## Whiteboard Process
![Class 01](../assest/class-01.jpeg)

## Approach & Efficiency
The approach of the solution is to create a new empty list called reversedArr of the same length as the input array. Then loop through the original array and set each element of the new array to the corresponding element from the original array. The index of each element in the new array is calculated as len(arr) - i - 1, which is the index of the current element in the original array counting from the end of the array. Finally, the function returns reversedArr, which contains the reversed elements of the original arr.


The time complexity of this solution is O(n), where n is the length of the input array. This is because the algorithm loops through the input array once to create the reversed array.

The space complexity of this solution is also O(n), since it creates a new array of the same length as the input array to store the reversed elements.


## Solution

def reverseArray(arr):

    reversedArr = [None] * len(arr)


    for i in range(len(arr)):

            reversedArr[len(arr) - i - 1] = arr[i]

    return reversedArr