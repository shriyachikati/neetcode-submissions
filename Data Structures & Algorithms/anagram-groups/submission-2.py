class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars_and_words = {}

        for word in strs:
            chars = ''.join(sorted(word))
            if chars in chars_and_words:
                chars_and_words[chars].append(word)
            else:
                chars_and_words[chars] = [word]
        return list(chars_and_words.values())