def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    lowercase_phrase = phrase.lower()
    begin_index = 0
    end_index = len(phrase) - 1

    while begin_index <= end_index:
        if lowercase_phrase[begin_index] == lowercase_phrase[end_index]:
            begin_index += 1
            end_index -= 1
        elif lowercase_phrase[begin_index] == ' ':
            begin_index += 1
        elif lowercase_phrase[end_index] == ' ':
            end_index -= 1
        else:
            # print('not palindrome')
            return False
        
    # print('A palindrome')
    return True


# Some More Tests  
# print(is_palindrome('Hello'))
# print(is_palindrome('on ahano'))
# print(is_palindrome('oihhi o'))
# print(is_palindrome('s kibwbi ks'))