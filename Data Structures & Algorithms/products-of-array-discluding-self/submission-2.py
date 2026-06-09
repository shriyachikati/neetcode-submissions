class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0
        output = []

        # Count the number of zeros and calculate the product without the zeros
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                product *= num

        # If there are more than two zeros in the array, the product becomes zero for every element
        if zeros > 1:
            return [0] * len(nums)

        # Get the output array
        for num in nums:
            if num == 0:
                output.append(product)
            elif zeros == 1:
                output.append(0)
            else:
                output.append(product // num)

        return output