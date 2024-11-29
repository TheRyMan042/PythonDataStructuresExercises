def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    most_common_num = 0
    seen = []
    for num in nums:
        count = nums.count(num)
        if num not in seen:
            if count > most_common_num:
                most_common_num = num
            seen.append(num)

    return most_common_num
    
    # Some More Tests
    # print(mode([1,2,4,2,1,4,5,2,1,6,3,2]))
    # print(mode([1,2,4,5,2,4,5,1,6,3,5]))
    # print(mode([1,2,3,4]))