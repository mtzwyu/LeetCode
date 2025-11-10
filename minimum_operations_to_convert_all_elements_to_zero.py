class Solution:
    def minOperations(nums):
        stack = [0] * (len(nums) + 1)
        top = 0
        ans = 0

        for num in nums:
            while stack[top] > num:
                top -= 1
                ans += 1
            if stack[top] != num:
                top += 1
                stack[top] = num

        return ans + top
    
print(Solution.minOperations([7, 2, 0, 4, 2]))  # Output: 4