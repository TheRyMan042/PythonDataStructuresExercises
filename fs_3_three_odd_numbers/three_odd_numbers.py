def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
    nums_length = len(nums)
    for index in range(nums_length):
        third_digit_index = index + 2
        second_digit_index = index + 1
        if third_digit_index < nums_length:
            total_sum = nums[index] + nums[second_digit_index] + nums[third_digit_index]
            if total_sum % 2 == 1:
                return True
            
    return False

# Some More Tests
# print(three_odd_numbers([1,3,5,7,9]))
# print(three_odd_numbers([2,4,6,8,10]))
# print(three_odd_numbers([3,7,14,5,13,9]))
# print(three_odd_numbers([3,7,14,5,13,8]))