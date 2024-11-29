def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    letter_phrase_list = list(phrase)
    letter_phrase_list.reverse()
    reversed_list = letter_phrase_list
    # print(letter_phrase_list)

    reversed_word = ''
    for char in reversed_list:
        reversed_word += char

    # print(reversed_word)
    return reversed_word

# Some more tests
# print(reverse_string('hello'))
# print(reverse_string('How are you doing?'))
# print(reverse_string('tacocat!'))
