def binary_search(arr, key):
    f = 0
    b = len(arr) - 1

    while f <= b:
        mid_arr = (f + b) // 2

        if arr[mid_arr] == key:
            return mid_arr
        elif arr[mid_arr] < key:
            f = mid_arr + 1
        else:
            b = mid_arr - 1

    return -1 