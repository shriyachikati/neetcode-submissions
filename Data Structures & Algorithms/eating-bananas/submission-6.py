import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Use binary search on the piles array for the eating speed
        piles.sort()
        l = 1
        r = piles[-1]
        output = r

        while l <= r:
            mid = l + (r - l) // 2

            time = 0
            for pile in piles:
                time += math.ceil(pile / mid)

            if time > h:
                l = mid + 1

            else:
                output = mid
                r = mid - 1

        return output