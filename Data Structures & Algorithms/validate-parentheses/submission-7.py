class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        if len(s) % 2 != 0:
            return False

        stack = []

        for p in s:
            if p not in parentheses:
                stack.append(p)
            else:
                if not stack:
                    return False
                if stack.pop() != parentheses[p]:
                    return False
        
        return not stack