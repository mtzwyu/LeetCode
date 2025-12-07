import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        counts = Counter(nums)
        
        for i, freq in counts.items():
            heapq.heappush(minHeap, (freq, i))
            
            if len(minHeap) > k:
                heapq.heappop(minHeap)
            
        return [i[1] for i in minHeap]
         




print(Solution().topKFrequent([5,3,1,1,1,3,5,73,1],3))