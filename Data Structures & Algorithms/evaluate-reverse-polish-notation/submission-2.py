class Solution:
    def calc(self, n1, n2, token):
        if token == '+':
            return n1 + n2
        elif token == '-':
            return n1 - n2
        elif token == '*':
            return n1 * n2
        elif token == '/':
            return int(n1 / n2)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = [];
        exp = set(['+', '-', '*', '/'])
        for token in tokens:
            if token in exp:
                n1 = stack.pop()
                n2 = stack.pop()
                res = self.calc(n2, n1, token)
                stack.append(res)
            else:
                stack.append(int(token));
        return stack[0];