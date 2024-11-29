def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowel_count = {}
    for letter in phrase.lower():
        if letter in 'aeiou':
            if letter in vowel_count:
                vowel_count[letter] += 1
            else: 
                vowel_count[letter] = 1

    # print('Vowels', vowel_count)
    return vowel_count

# Some More Tests
# print(vowel_count('blank'))
# print(vowel_count('Do you like movies?'))
# print(vowel_count('Deadpool and Wolverine'))