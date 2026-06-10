class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indexes = {num: i for i, num in enumerate(nums1)}
        stack = []
        output = [-1] * len(nums1)

        for num in nums2:
            while stack and (num > stack[-1]):
                output[indexes[stack.pop()]] = num

            if num in indexes:
                stack.append(num)
        
        return output