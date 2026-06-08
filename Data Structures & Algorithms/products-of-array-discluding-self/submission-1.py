class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0
        output = []

        for num in nums:
            if num == 0:
                zeros += 1
            else:
                product *= num

        if zeros > 1:
            return [0] * len(nums)

        for num in nums:
            if num == 0:
                output.append(product)
            elif zeros == 1:
                output.append(0)
            else:
                output.append(product//num)

        return output