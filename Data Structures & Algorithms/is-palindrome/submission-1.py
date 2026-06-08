import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = re.sub(r'[^0-9a-zA-Z]', '', s)
        return clean.lower()[::-1] == clean.lower()