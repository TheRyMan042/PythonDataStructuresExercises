def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    greater_numbers = 0
    decrease_index = 1

    if len(nums) <= 1:
        return greater_numbers
    
    for number in nums:
        # print('Main:', number)
        for index in range(decrease_index, len(nums)):
            # print('check:', nums[index])
            if nums[index] > number:
                greater_numbers += 1
        decrease_index += 1

    return greater_numbers

# Some More Tests
# print(find_greater_numbers([1,2,3]))
# print(find_greater_numbers([1,9,7,15]))
# print(find_greater_numbers([8]))
# print(find_greater_numbers([5,7]))
# print(find_greater_numbers([7,5]))