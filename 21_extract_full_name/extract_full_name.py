def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    full_names = []
    for person in people:
        for (key, name) in person.items():
            if key == 'first':
                # print('First Name:', name)
                first_name = name
            else:
                # print('Last Name:', name)
                last_name = name
        full_names.append(first_name + ' ' + last_name)
    
    # print(full_names)
    return full_names
        

# Another Test
# names = [
#     {'first': 'Steve', 'last': 'Jobs'},
#     {'first': 'Larry', 'last': 'King'},
#     {'first': 'Bill', 'last': 'Gates'},
#     {'first': 'Elon', 'last': 'Musk'}
# ]

# print(extract_full_names(names))