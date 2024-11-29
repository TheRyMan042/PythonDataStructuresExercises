def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    # print(lst.count(search_term))
    return lst.count(search_term)

# Some More Tests
# print([1,2,3,3,3,3,4,5,5].count(3))
# print([1,2,3,3,3,3,4,5,5].count(6))
# print([1,2,3,3,3,3,4,5,5].count(2))
# print([1,2,3,3,3,3,4,5,5].count(5))