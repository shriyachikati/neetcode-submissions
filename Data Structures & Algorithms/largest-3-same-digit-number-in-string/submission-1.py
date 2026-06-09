class Solution:
    def largestGoodInteger(self, num: str) -> str:
        output = ""
        for i in range(1, len(num) - 1):
            if num[i] == num[i - 1] == num[i + 1]:
                output = max(num[i-1:i+2], output)
        return output