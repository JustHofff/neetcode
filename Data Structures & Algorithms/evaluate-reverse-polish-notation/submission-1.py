class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for t in tokens:
            if t not in {'+', '-', '*', '/'}:
                s.append(t)
                continue
            
            r = int(s.pop())
            l = int(s.pop())
            
            if t == '+':
                res = l + r
            elif t == '-':
                res = l - r
            elif t == '*':
                res = l * r
            elif t == '/':
                res = l / r
            
            s.append(res)
        
        return int(s.pop())