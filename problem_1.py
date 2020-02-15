def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if type(number) != int:
        print("Please input an integer")
        return -1
    if number < 0:
        return None
    mid_number = number // 2
    min_number = 0
    max_number = number
    while min_number <= max_number:
        mid_number = min_number + (max_number - min_number) // 2
        target_number = mid_number * mid_number
        if target_number > number:
            if (mid_number - 1) * (mid_number - 1) < number:
                return mid_number - 1
            max_number = mid_number
        elif target_number < number:
            if (mid_number + 1) * (mid_number + 1) > number:
                return mid_number
            elif (mid_number + 1) * (mid_number + 1) == number:
                return mid_number + 1
            min_number = mid_number
        else:
            return mid_number


print("Pass" if (-1 == sqrt(9.0)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (8 == sqrt(80)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (None == sqrt(-5)) else "Fail")
