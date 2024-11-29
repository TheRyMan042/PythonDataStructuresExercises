def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    dict_keys = list(d.keys())
    dict_keys.sort()
    low_high_keys = (dict_keys[0], dict_keys[-1])
    return low_high_keys

# Some More Tests
# print(min_max_keys({3: 'what', 7: 'is', 5: 'this', 9: '?'}))
# print(min_max_keys({'appricot': 5, 'cherry': 4, 'peach': 4, 'blueberry': 5}))
# print(min_max_keys({3.5: 'not favorite', 7.5: 'favorite', 5.1: 'not favorite', 9.9: 'favorite', 15.0: 'favorite'}))