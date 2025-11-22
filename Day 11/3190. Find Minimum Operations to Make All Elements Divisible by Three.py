class Solution:
    def minimumOperations(nums: list[int]) -> int:
        res = 0
        for i in nums:
            if (i+1) % 3 == 0 or (i - 1) % 3 == 0:
                res +=1 
        return res

print(Solution.minimumOperations([1,2,3,4]))