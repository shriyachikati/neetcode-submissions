from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_chars = Counter(magazine)

        for char in ransomNote:
            if magazine_chars.get(char, 0) >= 1:
                magazine_chars[char] -= 1
            else:
                return False

        return True
