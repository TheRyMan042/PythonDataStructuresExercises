def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
    total = 0
    if end == None or end > len(nums):
        end = len(nums)
    else:
        end += 1

    for index in range(start, end):
        # print(nums[index])
        total += nums[index]
    # print(total)
    return total

# Some More Tests
# print(sum_range([5,10,15,20,25]))
# print(sum_range([5,10,15,20,25], 2))
# print(sum_range([5,10,15,20,25], end=2))
# print(sum_range([5,10,15,20,25], 1, 2))
# print(sum_range([5,10,15,20,25], 1, 100))