def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    list_index = 0
    new_list = []
    for item in lst:
        if list_index % 2 == 0:
            new_list.append(item)
        list_index += 1
    
    # print(lst)
    # print(new_list)
    return new_list

# Some More Tests
# print(remove_every_other([5,6,7,8,9]))
# print(remove_every_other([10,'hi',20,'there',30]))
# print(remove_every_other(['Hi','there','Mat','Pat','.']))
