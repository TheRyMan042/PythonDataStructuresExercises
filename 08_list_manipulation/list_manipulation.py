def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    begin_index = 0
    if command.lower() == 'remove':
        if location.lower() == 'beginning':
            removed_val = lst.pop(begin_index)
        elif location.lower() == 'end':
            removed_val = lst.pop()
        else:
            return None
        
        return removed_val
    
    elif command.lower() == 'add':
        if location.lower() == 'beginning':
            lst.insert(begin_index, value)
            # print('Value added:', value)
            # print(lst)
        elif location.lower() == 'end':
            lst.append(value)
        else:
            return None
        
        return lst
    
    else:
        return None

# Some More Tests
# print(list_manipulation([1,2,3], 'Add', 'BeGiNnInG', 0))
# print(list_manipulation([1,2,3], 'Add', 'End', 4))
# print(list_manipulation([4,10,14], 'Add', 'Beginning', 20))
# print(list_manipulation([-35,5,10,15], 'Remove', 'Beginning'))
# print(list_manipulation([25,50,75,100], 'Remove', 'End'))
