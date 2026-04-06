def isValid(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map:  # Closing bracket
            if not stack or stack.pop() != bracket_map[char]:
                return False
        else:  # Opening bracket
            stack.append(char)

    return not stack


# Test examples
print(isValid("()"))       # True
print(isValid("()[]{}"))   # True
print(isValid("(]"))       # False
print(isValid("([])"))     # True
print(isValid("([)]"))     # False
