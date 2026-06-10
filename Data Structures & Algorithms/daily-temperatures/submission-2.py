class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        tempStack = []
        iStack = []

        for i, temperature in enumerate(temperatures):
            while tempStack and (temperature > tempStack[-1]):
                tempStack.pop()
                j = iStack.pop()
                result[j] = i - j
            if not tempStack or (temperature <= tempStack[-1]):
                tempStack.append(temperature)
                iStack.append(i)

        return result
