class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Brute force approach - two pointers
        new_arr = []
        for i in range(len(arr)-1):
            max_num = 0
            # Search for the highest number and store it in a variable
            for j in range(i+1, len(arr)):
                if arr[j] >= max_num:
                    max_num = arr[j]
            new_arr.append(max_num)
        new_arr.append(-1)

        return new_arr