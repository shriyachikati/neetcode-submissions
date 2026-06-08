class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mappings = {}
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            # Check if the s character is in the dictionary
            if s_char in mappings:
                # If the mapping is incorrect, return false
                if mappings[s_char] != t_char:
                    return False
            else:
                # Check if the mapped value is in the dictionary
                if t_char in mappings.values():
                    return False

                mappings[s_char] = t_char
        return True