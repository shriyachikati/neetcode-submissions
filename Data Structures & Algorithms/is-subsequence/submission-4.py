class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # # Brute force approach
        # # Base case
        # if len(s) > len(t):
        #     return False

        # last_idx = -1
        # for s_char in s:
        #     if last_idx == len(t) - 1:
        #         return False
        #     for i in range(last_idx + 1, len(t)):
        #         if s_char == t[i]:
        #             last_idx = i
        #             break
        #         elif i == len(t)-1:
        #             return False
        # return True

        # Two pointers
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)