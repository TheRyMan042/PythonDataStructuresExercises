def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    if len(lst) == 0:
        # print('None')
        return None
    else:
        # print(lst[-1])
        return lst[-1]

# Some More Tests
# print(last_element([1,5,0,7,0]))
# print(last_element([1,5,7,9,13]))