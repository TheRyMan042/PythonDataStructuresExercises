def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_phrase = ''
    
    for letter in phrase:
        if letter == to_swap.upper() or letter == to_swap.lower():
            if letter.isupper():
                new_phrase += letter.lower()
            elif letter.islower():
                new_phrase += letter.upper()
        else:
            new_phrase += letter

    # print(new_phrase)
    return new_phrase
    
# Some More Tests
# print(flip_case('hhheelppp', 'h'))
# print(flip_case('hhheelppp', 'P'))
# print(flip_case('hhheelppp', 'y'))
# print(flip_case('AAAAbbbbbaaa', 'A'))
