from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if len(stack) == 0: return False
                char = stack.pop()
                if (c == ')' and char != '(') or (c == ']' and char != '[') or (c == '}' and char != '{'):
                    return False
        if len(stack) > 0: return False
        return True