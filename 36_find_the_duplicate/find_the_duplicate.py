def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    seen = [];
    for num in nums:
        if num not in seen:
            seen.append(num)
        else:
            # print('duplicate')
            return num
    return None


# Some More Tests
# print(find_the_duplicate([1,2,3,4,1,5]))
# print(find_the_duplicate([4,11,15,21,35,40,56]))
# print(find_the_duplicate([42,11,15,21,35,42,56]))