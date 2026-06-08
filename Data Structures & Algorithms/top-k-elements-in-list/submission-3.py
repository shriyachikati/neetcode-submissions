class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        counts_tuples = sorted(list(counts.items()), key=lambda x: x[1], reverse=True)
        return [value for value, count in counts_tuples[:k]]