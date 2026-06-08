class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mappings1 = {}
        mappings2 = {}
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            # Check if the s character is in the dictionary and if the mapped value matches
            if ((s_char in mappings1) and (mappings1[s_char] != t_char)) or ((t_char in mappings2) and mappings2[t_char] != s_char):
                return False
            else:
                mappings1[s_char] = t_char
                mappings2[t_char] = s_char
        return True