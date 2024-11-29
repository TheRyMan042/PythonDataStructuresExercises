def triple_and_filter(nums):
    """Return new list of tripled nums for those nums divisible by 4.

    Return every number in list that is divisible by 4 in a new list,
    except multipled by 3.
    
        >>> triple_and_filter([1, 2, 3, 4])
        [12]
        
        >>> triple_and_filter([6, 8, 10, 12])
        [24, 36]
        
        >>> triple_and_filter([1, 2])
        []
    """
    mults_of_4 = [num for num in nums if num % 4 == 0]
    added_index = 0
    for num in mults_of_4:
        mults_of_4[added_index] = num * 3
        added_index += 1
    return mults_of_4


# Some More Tests
# print(triple_and_filter([1,2,4,8,16]))
# print(triple_and_filter([1,2,6,24,120]))
# print(triple_and_filter([1,2,3,5,6,7]))