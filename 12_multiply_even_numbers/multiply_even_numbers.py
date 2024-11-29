def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    total = 1

    for num in nums:
        if num % 2 == 0:
            total *= num
    
    # print(total)
    return total

# Some More Tests
# print(multiply_even_numbers([1,2,3,4,8,9,10]))
# print(multiply_even_numbers([3,9,15,21]))
# print(multiply_even_numbers([3,9,12,15,21]))
