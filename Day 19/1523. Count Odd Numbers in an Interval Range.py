# class Solution:
#     def countOdds(self, low: int, high: int) -> int:
#         if high == low and (high %2 == 0 or low % 2 == 0):
#             return 0
#         if (high - low + 1) % 2 == 0:
#             return (high+1 - low +1) //2
#         if high % 2 == 0 and low % 2 == 0:
#             return (high - low) // 2     
        
#         return (high - low +2)//2






class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return ((high+1)//2)-(low//2)
        
print(Solution().countOdds(6 , 12))



