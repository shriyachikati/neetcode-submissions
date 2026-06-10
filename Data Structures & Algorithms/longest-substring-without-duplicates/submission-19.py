class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # output = 0
        # for i in range(len(s)):
        #     seen = set()
        #     length = 0
        #     for j in range(i, len(s)):
        #         if s[j] not in seen:
        #             seen.add(s[j])
        #             length += 1
        #             output = max(output, length)
        #         else:
        #             break
        # return output


        seen = set()
        l = 0
        output = 0

        # Loop through the indexes of the string
        for r in range(len(s)):
            # If we've already seen the character, remove the character at the start of the window and move the left pointer
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            output = max(output, r - l + 1)

        return output