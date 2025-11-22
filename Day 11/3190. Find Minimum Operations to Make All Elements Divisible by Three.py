class Solution:
    def minimumOperations(nums: list[int]) -> int:
        return sum(1 for i in nums if i % 3 == 2 or i % 3 == 1)

print(Solution.minimumOperations([1,2,3,4]))