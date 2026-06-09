class Solution:
    def longestPalindrome(self, s: str) -> int:
        mp = {}

        for char in s:
            if char in mp:
                mp[char] += 1
            else:
                mp[char] = 1

        output = 0
        odd = 0
        for value in mp.values():
            if value % 2 == 0:
                output += value
            else:
                output += (value // 2) * 2
                if not odd:
                    odd = 1
        output += odd
        return output


