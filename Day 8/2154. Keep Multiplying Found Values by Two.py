class Solution:
    def findFinalValue(nums: list[int], original: int) -> int:
        for i in nums:
            if original == i:
                return Solution.findFinalValue(nums, original * 2)
        return original
    
print(Solution.findFinalValue(nums = [5,3,6,1,12], original = 3))