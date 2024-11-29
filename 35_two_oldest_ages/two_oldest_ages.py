def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)
    """

    # NOTE: don't worry about an optimized runtime here; it's fine if
    # you have a runtime worse than O(n)

    # NOTE: you can sort lists with lst.sort(), which works in place (mutates);
    # you may find it helpful to research the `sorted(iter)` function, which
    # can take *any* type of list-like-thing, and returns a new, sorted list
    # from it.
    ages.sort(reverse = True)
    for index in range(1, len(ages)):
        first_oldest = ages[0]
        second_oldest = ages[index]
        if second_oldest != first_oldest:
            two_unique_oldest = (second_oldest, first_oldest)
            return two_unique_oldest
        
# Some More Tests
# print(two_oldest_ages([17,25,11,4,1,15]))
# print(two_oldest_ages([2,5,9,10,10,11,11]))
# print(two_oldest_ages([2,6,8,10,11,16,16,21]))