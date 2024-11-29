def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    paren_order = list(parens)
    index = 0

    for char in parens:
        if char == ')':
            right_paren_index = index
            if right_paren_index > 0 and parens[right_paren_index - 1] == '(':
                paren_order.pop(right_paren_index)
                paren_order.pop(right_paren_index - 1)
                index -= 2
        index += 1
    
    # print(paren_order)
    if len(paren_order) == 0:
        return True
    else:
        return False


# Some More Tests
valid_parentheses('()')
valid_parentheses('()(')
valid_parentheses(')()')
valid_parentheses(')()(')
valid_parentheses('()()')
valid_parentheses('(()()')
valid_parentheses('(()())')