class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = {}
        for num in nums:
            if num in mp:
                mp[num] += 1
            else:
                mp[num] = 1
            if mp[num] > (len(nums) // 2):
                return num