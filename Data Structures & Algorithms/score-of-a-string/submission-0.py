class Solution:
    def scoreOfString(self, s: str) -> int:
        i = 0
        value = 0
        while i < len(s) - 1:
            value += abs(ord(s[i]) - ord(s[i+1]))
            i += 1
        return value