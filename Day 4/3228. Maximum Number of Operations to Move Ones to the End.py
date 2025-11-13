class Solution:
    def maxOperations(s: str):
        ones = [len(i) for i in s.split('0') if i]
        print(ones)
        if not ones:
            return 0
        tot = 0
        ans = 0
        for f in ones[:-1]:
            tot += f
            ans += tot
            print(tot, ans)
        if s[-1] == '1':
            return ans
        return ans + tot + ones[-1]
            
                
            
        
            


            


print(Solution.maxOperations("10"))  # Output: 1