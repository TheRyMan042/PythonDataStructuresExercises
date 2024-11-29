def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    friendA_set = set(a[2])
    friendB_set = set(b[2])

    if (friendA_set & friendB_set):
        return True
    else:
        return False

# Some More Tests
# arnold = ('Arnold', 16, ['social media', 'footbal'])
# johnny = ('Johnny', 19, ['social media', 'hockey', 'chess'])
# david = ('David', 24, ['chess', 'reading'])

# print(friend_date(arnold, johnny))
# print(friend_date(arnold, david))
# print(friend_date(johnny, david))