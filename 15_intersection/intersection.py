def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    set1 = set(l1)
    set2 = set(l2)
    my_intersection_set = set1 & set2
    my_intersection = list(my_intersection_set)
    # print(set1 & set2)
    # print(my_intersection)
    return my_intersection

# Some More Tests
# print(intersection([1,2,3,4], [2,4,6,8]))
# print(intersection([1,4,8,16], [2,4,6,8]))
# print(intersection([1,2,3,4], [5,6,7,8]))