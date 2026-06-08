class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lengths = [len(string) for string in strs]
        min_length = min(lengths)
        output = ''

        if len(strs) == 1:
            return strs[0]
            
        for i in range(min_length):
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j+1][i]:
                    return output
            output += strs[j][i]

        return output