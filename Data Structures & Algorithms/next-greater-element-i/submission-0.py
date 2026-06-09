class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = [-1] * len(nums1)
        for i, num1 in enumerate(nums1):
            j = nums2.index(num1)
            req = None
            while j < len(nums2):
                if nums2[j] > num1:
                    output[i] = nums2[j]
                    break
                j += 1

        return output                
                