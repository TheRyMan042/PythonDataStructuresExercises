def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    lowercase_word = word.lower()
    lowercase_letter = letter.lower()

    # print(lowercase_word.count(lowercase_letter))
    return lowercase_word.count(lowercase_letter)

# Some More Tests
# print(single_letter_count('Now is the time to be ALIVEEEEE!!!', 'e'))
# print(single_letter_count('Now is the time to be ALIVEEEEE!!!', 'a'))
# print(single_letter_count('Now is the time to be ALIVEEEEE!!!', 'W'))
# print(single_letter_count('Now is the time to be ALIVEEEEE!!!', '!'))