def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    letter_count = {}
    for letter in phrase:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1

    # print(letter_count)
    return (letter_count)

# Some More Tests
# print(multiple_letter_count('Well hEllo thEre'))
# print(multiple_letter_count('my Oh My oH my OH mY Oh my'))