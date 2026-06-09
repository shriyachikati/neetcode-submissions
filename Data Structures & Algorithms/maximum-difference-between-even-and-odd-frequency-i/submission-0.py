class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}

        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        # We just need the biggest odd frequency and the smallest even frequency
        odd = 0
        even = 1000
        for value in freq.values():
            if value % 2 == 0:
                even = min(even, value)
            else:
                odd = max(odd, value)

        return odd - even
