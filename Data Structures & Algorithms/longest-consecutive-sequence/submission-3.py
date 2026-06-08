class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        longest = 1
        current = 1

        if len(nums) == 0:
            return 0

        for i in range(len(nums_sorted) - 1):
            if nums_sorted[i + 1] - nums_sorted[i] == 1:
                current += 1
                longest = max(current, longest)
            elif nums_sorted[i + 1] - nums_sorted[i] == 0:
                continue
            else:
                current = 1
                
        return longest