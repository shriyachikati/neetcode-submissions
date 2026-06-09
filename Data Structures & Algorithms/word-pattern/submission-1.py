class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_p_s = {}
        map_s_p = {}

        s_arr = s.split()

        if len(pattern) != len(s_arr):
            return False

        for i in range(len(pattern)):
            char = pattern[i]
            word = s_arr[i]
            if ((char in map_p_s) and (map_p_s[char] != word)) or \
                ((word in map_s_p) and (map_s_p[word] != char)):
                return False
            else:
                if char not in map_p_s:
                    map_p_s[char] = word
                    map_s_p[word] = char

        return True