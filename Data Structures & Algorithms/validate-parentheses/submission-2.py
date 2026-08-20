class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {'(': ')', '{': '}', '[': ']'}
        for c in s:
            if c in parentheses:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False;
                last_braces = stack.pop();
                eq_close_braces = parentheses[last_braces];
                if (eq_close_braces != c):
                    return False;
        return len(stack) == 0;