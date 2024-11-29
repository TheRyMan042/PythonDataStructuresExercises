def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    if (type(a) is not str and type(b) is not str):
        if a > b:
            # print('First is greater')
            return 'First is greater'
        elif b > a:
            # print('Second is greater')
            return 'Second is greater'
        else:
            # print('Numbers are equal')
            return 'Numbers are equal'

# Some More Tests
# print(number_compare(1,3))
# print(number_compare(3.5,1.2))
# print(number_compare(-23,-51))
# print(number_compare(0,0))
