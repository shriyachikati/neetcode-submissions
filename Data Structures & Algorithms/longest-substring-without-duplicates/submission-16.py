class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0

        for i in range(len(s)):
            seen = set()
            length = 0
            for j in range(i, len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                    length += 1
                    output = max(output, length)
                else:
                    break

        return output
                    