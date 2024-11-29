def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which are not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    >>> reverse_vowels("aeiou")
    'uoiea'

    >>> reverse_vowels("why try, shy fly?")
    'why try, shy fly?'
    """
    s_list = list(s)
    word_len = len(s_list)
    vowels = 'aeiouAEIOU'
    if word_len % 2 != 0:
        middle_index = word_len // 2
    elif word_len % 2 == 0:
        middle_index = word_len // 2 - 1
    else:
        return ''
 
    right_index = word_len - 1
    left_index = 0
    for index in range(word_len):
        # print('Left:', left_index)
        # print('Right:', right_index)
        # print('Left:', s_list[left_index])
        # print('Right:', s_list[right_index])
        if s_list[left_index] in vowels:
            # print('found left vowel')
            while s_list[right_index] not in vowels:
                right_index -= 1
            # print('found right vowel, now reverse it')
            # print('Right:', right_index)
            # print('Right:', s_list[right_index], '\n')
            temp = s_list[right_index]
            s_list[right_index] = s_list[left_index]
            s_list[left_index] = temp 
        elif s_list[right_index] in vowels:
            # print('found right vowel')
            while s_list[left_index] not in vowels:
                left_index += 1
            # print('found left vowel, now reverse it')
            # print('Left:', left_index)
            # print('Left:', s_list[left_index], '\n')
            temp = s_list[right_index]
            s_list[right_index] = s_list[left_index]
            s_list[left_index] = temp 

        if left_index >= middle_index or left_index >= right_index:
            break
        
        right_index -= 1
        left_index += 1

    # print(s_list)
    changed_str = ''.join(s_list)
    # print(changed_str)
    return changed_str

    
# Some More Tests
reverse_vowels('Hello')
reverse_vowels('Engine')
reverse_vowels('Oh my goodness')
reverse_vowels("Reverse Vowels In A String")