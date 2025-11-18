class Solution:
    def containsDuplicate(nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
        



print(Solution.containsDuplicate([1,2,3,3]))  # True