class Solution:
    def largestGoodInteger(self, num: str) -> str:
        output = ""
        for i in range(1, len(num) - 1):
            if num[i] == num[i - 1] == num[i + 1]:
                output = max(f"{num[i]}" * 3, output)
        return output