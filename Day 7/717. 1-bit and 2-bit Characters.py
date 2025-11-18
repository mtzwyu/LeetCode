class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        n = len(bits)
        i =0 
        while i < n - 1:
            if bits[i] == 0:
                i += 1
            else:
                i += 2
        return i == n - 1


print(Solution.isOneBitCharacter(Solution, [1,0,0]))  # True
print(Solution.isOneBitCharacter(Solution, [1,1,1,0]))  # False 