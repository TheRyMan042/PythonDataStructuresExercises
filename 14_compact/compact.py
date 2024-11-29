def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    truthy_list = []
    for item in lst:
        if item:
            truthy_list.append(item)

    # print(truthy_list)
    return truthy_list

# Some More Tests
# print(compact([1,2,0,3,0.5,0.0,'',"hi","",{}]))
# print(compact([[1,2,3],'',[],"",{'wins': 1}, ()]))