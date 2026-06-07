class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # output = [0] * 2
        # for i in range(len(nums)):
        #     required = target - nums[i]
        #     if required in nums[i+1:]:
        #         output[0] = i
        #         output[1] = nums.index(required, i+1)
        #         break
        # return output


        # Using a dictionary for easy lookups
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in seen:
                return [seen[diff], i]
            seen[num] = i