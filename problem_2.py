def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 0:
        print("Please input a valid array.")
        return -1
    min_number_index = find_min_number_index(input_list)
    if number > input_list[0]:
        return binary_search(input_list, number, 0, min_number_index - 1)
    elif number < input_list[0]:
        return binary_search(input_list, number, min_number_index, len(input_list) - 1)
    else:
        return 0


def binary_search(input_list, number, left, right):
    low = left
    hight = right
    while low <= hight:
        mid = low + ((hight - low) >> 1)
        if input_list[mid] == number:
            return mid
        elif input_list[mid] < number:
            low = mid + 1
        else:
            hight = mid - 1
    return -1


def find_min_number_index(input_list):
    low = 0
    hight = len(input_list) - 1
    if input_list[low] < input_list[hight]:
        return 0

    while low <= hight:
        mid = low + ((hight - low) >> 1)
        if input_list[low] < input_list[mid]:
            if input_list[mid + 1] < input_list[mid]:
                return mid + 1
            low = mid + 1
        elif input_list[low] > input_list[mid]:
            if input_list[mid - 1] > input_list[mid]:
                return mid
            hight = mid - 1
        else:
            return mid


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[1, 2, 3, 4, 6, 7, 8], 1])
test_function([[1], 0])
test_function([[], 1])
