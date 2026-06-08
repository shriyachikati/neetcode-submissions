class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Sort the array to make it easier to compare
        nums_sorted = sorted(nums)
        longest = 1
        current = 1

        # Return 0 if it is an empty array
        if len(nums) == 0:
            return 0

        # Loop through the array
        for i in range(len(nums_sorted) - 1):
            # Check for the difference between adjacent elements and update accordingly
            if nums_sorted[i + 1] - nums_sorted[i] == 1:
                current += 1
                longest = max(current, longest)
            elif nums_sorted[i + 1] - nums_sorted[i] == 0:
                continue
            else:
                current = 1
                
        return longest