def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_str = str(num1)
    num2_str = str(num2)
    seen = [];

    for num in num1_str:
        if num not in seen:
            if num1_str.count(num) != num2_str.count(num):
                # print('False')
                return False

    # print('True')
    return True

# Some More Tests
# print(same_frequency(1234,5678))
# print(same_frequency(12341,56781))
# print(same_frequency(123321,321123))