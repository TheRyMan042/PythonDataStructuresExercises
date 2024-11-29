def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    repeated_str = ''
    if type(num) is int and num >= 0:
        count = 0
        while count < num:
            repeated_str += phrase
            count += 1
        # print('Word:', repeated_str)
        return repeated_str
    else:
        # print('None')
        return None

# Some More Tests
# print(repeat('el',2))
# print(repeat(")(",7))
# print(repeat(":')",7))
# print(repeat('nothing... ', -4))
# print(repeat('nothing... ', 'none'))