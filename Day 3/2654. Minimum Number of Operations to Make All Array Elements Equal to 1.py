import math
from math import gcd
class Solution:
    def minOperations(nums: list[int]):
        n = len(nums)
        num1 = 0
        g = 0

        for x in nums:
            if x == 1:
                num1 += 1
            g = gcd(g, x)
            # print(g)

        if num1 > 0:
            return n - num1
        if g > 1:
            return -1

        min_len = n
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                print(g)
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    print("min_len: ", min_len)
                    break

        return min_len + n - 2
            

print(Solution.minOperations([2,6,3,4]))  # Output: 4
        
                