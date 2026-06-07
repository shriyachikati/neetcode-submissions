class Solution:
    def countSeniors(self, details: List[str]) -> int:
        num = 0
        for detail in details:
            if int(detail[11:13]) > 60:
                num += 1
        return num