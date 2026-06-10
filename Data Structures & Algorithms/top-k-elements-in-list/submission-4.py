from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        counts_sorted = sorted(list(counts.items()), key=lambda x: x[1], reverse=True)
        return [key for key, value in counts_sorted[:k]]