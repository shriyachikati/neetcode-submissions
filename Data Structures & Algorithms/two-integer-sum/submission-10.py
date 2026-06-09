class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for j, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], j]
            seen[num] = j