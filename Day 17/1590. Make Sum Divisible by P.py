class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        if sum(nums)%p==0:
            return 0
        target = sum(nums) % p
        dic,n = {0:-1},len(nums)
        cur,ret = 0,n
        for i,num in enumerate(nums):
            cur = (cur+num)%p
            if dic.get((cur-target)%p) is not None:
                ret = min(ret,i-dic.get((cur-target)%p))
            dic[cur] = i
        return ret if ret < n else -1
    

            
        
        
        
        
        
        
        
print(Solution().minSubarray(nums = [3,1,4,2], p = 6))# output 1
print(Solution().minSubarray(nums = [6,3,5,2], p = 9))# output 2
print(Solution().minSubarray(nums = [1,2,3], p = 3))# output 0
