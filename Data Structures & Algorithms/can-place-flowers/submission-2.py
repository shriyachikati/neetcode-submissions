class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        possible = 0

        if n == 0:
            return True
        # Base case
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                if n <= 1:
                    return True
            
            return False

        else:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                possible += 1
                flowerbed[0] = 1

            for i in range(1, len(flowerbed) - 1):
                if flowerbed[i] == 0:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        possible += 1
                        flowerbed[i] = 1
                        
            if flowerbed[-1] == 0 and flowerbed[-2] == 0:
                possible += 1
                flowerbed[-1] = 0

        if possible >= n:
            return True
        
        return False