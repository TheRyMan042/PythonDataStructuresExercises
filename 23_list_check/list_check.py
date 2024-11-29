def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    for item in lst:
        if not isinstance(item, list):
            return False
    return True
        
# Some More Tests
# print(list_check([[1,2],[3,4],[5,6]]))
# print(list_check([[1,2.5],[True],[5,{}],[]]))
# print(list_check([[1,2.5],[True],[5,{}],[], 5]))

