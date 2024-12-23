def binary_search(arr, target):
    sorted_array = sorted(arr)
    left_index = 0
    right_index = len(sorted_array) - 1

    while  left_index<= right_index:
        
        middle_index = (left_index + right_index) // 2  

        if sorted_array[middle_index] == target:
            return middle_index

        elif sorted_array[middle_index] > target:
            right_index = middle_index - 1

        else:
            left_index = middle_index + 1

    # Target is not found in the array
    return -1

array = [1, 4, 7, 11, 15]
search = 11
index = binary_search(array, search)
print(f"Target {search} is at index: {index}")
