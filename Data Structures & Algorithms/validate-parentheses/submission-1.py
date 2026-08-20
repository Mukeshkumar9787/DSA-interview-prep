class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {'(': ')', '{': '}', '[': ']'}
        for c in s:
            if c in parentheses:
                stack.append(c)
            else:
                if len(stack) == 0 or parentheses[stack.pop()] != c:
                    return False;
        return len(stack) == 0;