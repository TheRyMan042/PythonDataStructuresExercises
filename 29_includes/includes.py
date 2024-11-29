def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    if type(collection) is dict:
        # print("A set or dict, don't use start; just search")
        if sought in collection.values():
            # print(f"{sought} is in values collection")
            return True
        else:
            return False
    elif type(collection) is set:
        for item in collection:
            if sought == item:
                return True
        return False
    else:
        # print('\nlook from certain index')
        if start == None:
            # print('run from beginning')
            # print(len(collection))
            if sought in collection:
                # print(f"{sought} is in collection")
                return True
            else:
                # print(f"No {sought} in collection")
                return False
        else:
            for index in range(start, len(collection)):
                if type(collection) is str: 
                    # print(collection[index:index+len(sought)])
                    split_str = collection[index:index+len(sought)]
                    if split_str == sought:
                        # print(f"{sought} found")
                        return True
                    # else:
                    #     print(f"No {sought}")
                elif collection[index] == sought:
                    # print(f"{sought} found")
                    # break
                    return True
                # else:
                #     print(f"No {sought}")
            return False

# Some More Tests

# No start
# print(includes({'a': 1, 'b': 2, 'c': '?'}, 2))
# print(includes({'hi', 'there', 'user', 1, 2, 3, 4.5, 6.7}, 'user'))
# print(includes({'hi', 'there', 'user', 1, 2, 3, 4.5, 6.7}, 5))
# print(includes('hello there', 'l'))
# print(includes('hello there', 'llo'))
# print(includes('hello there', 'x'))
# print(includes(['a', 'b', 'c', 'd', 1, 2, 3, 4, 10.0, 11.5], 3))
# print(includes(['a', 'b', 'c', 'd', 1, 2, 3, 4, 10.0, 11.5], 'c'))
# print(includes(['a', 'b', 'c', 'd', 1, 2, 3, 4, 10.0, 11.5], 11.5))
# print(includes(['a', 'b', 'c', 'd', 1, 2, 3, 4, 10.0, 11.5], 12.5))
# print(includes(['a', 'b', 'c', 'd', 1, 2, 3, 4, 10.0, 11.5], '3'))
# print(includes((1,2,3,'z','y','x',5.5,'10.5',2.2), 3))
# print(includes((1,2,3,'z','y','x',5.5,'10.5',2.2), '10.5'))
# print(includes((1,2,3,'z','y','x',5.5,'10.5',2.2), 'y'))
# print(includes((1,2,3,'z','y','x',5.5,'10.5',2.2), 4))
# print(includes((1,2,3,'z','y','x',5.5,'10.5',2.2), 'h'))

# With start
# print(includes((1,2,3,'z',2, 'y',3,'x',5.5, 3,'10.5',2.2, 'x', 2.2), 3, 4))
# print(includes((1,2,3,'z',2, 'y',3,'x',5.5, 3,'10.5',2.2, 'x', 2.2), 3, 10))
# print(includes(['a', 'b', 'b', 'c', 1, 'd', 1, 'd', 2, 3, 'b', 4, 10.0, 1, 11.5], 'd', 3))
# print(includes(['a', 'b', 'b', 'c', 1, 'd', 1, 'd', 2, 3, 'b', 4, 10.0, 1, 11.5], 'd', 6))
# print(includes(['a', 'b', 'b', 'c', 1, 'd', 1, 'd', 2, 3, 'b', 4, 10.0, 1, 11.5], '1', 3))
# print(includes('hello there', 'llo', 1))
# print(includes('hello there', 'llo', 3))
# print(includes('hello there', 'e', 8))
