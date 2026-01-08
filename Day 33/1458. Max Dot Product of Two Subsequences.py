from typing import List
import math

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [-math.inf] * (m + 1)
        for i in range(n):
            prev_dp = dp[:]
            for j in range(m):
                product = nums1[i] * nums2[j]
                current_max = max(product, product + prev_dp[j])
                dp[j+1] = max(prev_dp[j+1], dp[j], current_max)
                
        return dp[m]