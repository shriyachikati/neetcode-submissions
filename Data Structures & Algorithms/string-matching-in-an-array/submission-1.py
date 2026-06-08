class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        output = []
        for word in words:
            for word2 in words:
                if (word != word2) and (word in word2) and (word not in output):
                    output.append(word)

        return output