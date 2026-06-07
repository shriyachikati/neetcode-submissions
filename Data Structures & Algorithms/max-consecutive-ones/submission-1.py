class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # ones = (''.join(map(str, nums))).split('0')
        # return len(max(ones))

        # Iteration
        count = 0
        max_count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                count = 0
            max_count = max(count, max_count)
        return max_count
