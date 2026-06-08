class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]

        for i in range(numRows - 1):
            new = []
            new.append(1)
            for k in range(len(output[-1])-1):
                new.append(output[-1][k] + output[-1][k+1])
            new.append(1)
            output.append(new)

        return output