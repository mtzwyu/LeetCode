class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for k in range(1, 4): 
                if i + k < len(nums) and nums[i] == nums[i + k]:
                    return nums[i]
        return -1