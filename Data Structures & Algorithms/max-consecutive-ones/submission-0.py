class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = (''.join(map(str, nums))).split('0')
        return len(max(ones))