from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices) # n = 3
        m = k // 2 # m = 1, k = 2
        
        A = [strategy[i] * prices[i] for i in range(n)]
        base = sum(A) # base = 9
        
        sumA = sum(A[:k]) # sumA = 9
        sumP2 = sum(prices[m:k])  # sumP2 = 4
        bestDelta = sumP2 - sumA# bestDelta = -5
        
        for l in range(1, n - k + 1):
            sumA += A[l + k - 1] - A[l - 1] # SumA = 9 + 0 -5 = 4
            sumP2 += prices[l + k - 1] - prices[l + m - 1] # SumP2 = 4 + 3 - 4 = 3
            cur = sumP2 - sumA
            if cur >bestDelta:
                bestDelta = cur
        
        if bestDelta < 0:
            bestDelta = 0

        return base + bestDelta
        
print(Solution().maxProfit(prices = [5,4,3], strategy = [1,1,0], k = 2))