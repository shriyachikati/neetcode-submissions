class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Initialize two pointers
        i = 0
        j = len(heights) - 1

        # Set a variable for the max amount of water
        max_amount = 0

        while i < j:
            # The amount of water is calculated by the width times the height
            amount = (j - i) * (min(heights[i], heights[j]))
            max_amount = max(amount, max_amount)

            # The amount of water stored is dependent on the lower bar of the two
            # So, move the current pointer if it is pointing at the lower bar
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1

        return max_amount