class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        possible = 0

        # If the required number of plots is zero, return True
        if n == 0:
            return True
        
        # Check if there is only one plot
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                if n <= 1:
                    return True
            
            return False

        else:
            # Check for if the first and second plots are empty
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                possible += 1
                # Plant the flower
                flowerbed[0] = 1

            for i in range(1, len(flowerbed) - 1):
                if flowerbed[i] == 0:
                    # Check if the adjacent plots of the empty plot are empty
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        possible += 1
                        # Plant the flower
                        flowerbed[i] = 1
            
            # Check if the last plot is empty and its adjacent plot is also empty
            if flowerbed[-1] == 0 and flowerbed[-2] == 0:
                possible += 1
                # Plant the flower
                flowerbed[-1] = 1

        # If the planted fields are greater than or equal to the required number, return True
        if possible >= n:
            return True
        
        return False