class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Locate the pivot (where the array was rotated)
        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l

        # Binary search
        def binary_search(l, r, nums):
            while l <= r:
                m = l + (r - l) // 2

                if target < nums[m]:
                    r = m - 1
                elif target > nums[m]:
                    l = m + 1
                else:
                    return m
            
            return -1

        # Check the left part of the array for the target
        result = binary_search(0, pivot - 1, nums)

        if result != -1:
            return result
            
        # If the target is not found, search the right part of the array
        return binary_search(pivot, len(nums) - 1, nums) 