def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    factors = [1, num] #will always factor itself by one
    begin_index = 1
    for divisor in range(2, num + 1):
        middle_index = len(factors) - begin_index #gets the middle index
        quotient = int(num / divisor)
        if divisor < quotient:
            if num % divisor == 0:
                factors.insert(middle_index, quotient)
                factors.insert(begin_index, divisor)
                begin_index += 1

    
    # print(factors)
    return factors
            
# Some More Tests
# print(find_factors(10))
# print(find_factors(321421))
# print(find_factors(11))
# print(find_factors(48))
# print(find_factors(100))
# print(find_factors(101))
# print(find_factors(1000))