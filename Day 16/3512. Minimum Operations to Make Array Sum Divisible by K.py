class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        tong = sum(nums)
        if tong < k:
            return tong
        mod = tong % k
        if mod == 0:
            return 0
        for i in nums:
            if i < mod:
                continue
            return  
        
        

print(Solution().minOperations([3,9,7], k = 5))