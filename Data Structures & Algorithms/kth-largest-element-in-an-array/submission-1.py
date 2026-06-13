import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_neg = [-num for num in nums]
        heapq.heapify(nums_neg)

        for i in range(k):
            output = heapq.heappop(nums_neg)

        return -output