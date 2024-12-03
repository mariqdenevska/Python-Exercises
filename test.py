def binary_search(array, target):
    sorted_array = sorted(array)
    left_index = 0
    right_index = len(sorted_array) - 1

    while  left_index<= right_index:
        # Find the middle index
        middle_index = (left_index + right_index) // 2  

        # Check if the target is at the middle
        if sorted_array[middle_index] == target:
            return middle_index

        elif sorted_array[middle_index] > target:
            right_index = middle_index - 1

        else:
            left_index = middle_index + 1

    # Target is not found in the array
    return -1

array = [1, 4, 7, 11, 15]
target = 11
index = binary_search(array, target)
print(f"Target {target} is at index: {index}")
