class Solution:  
    def validateCoupons(self, code: List[str], businessLine: List[str],isActive: List[bool]) -> List[str]:

        def isValid(record):
            return (record[0] in valid_business and record[2] and record[1].replace('_', 'a').isalnum())

        valid_business = {"electronics", "grocery", "restaurant", "pharmacy"}

        ans = sorted(filter(isValid, zip(businessLine, code, isActive)))
        return [coupId for _, coupId, _ in ans]
    
    
print(Solution().validateCoupons(["GROCERY15","ELECTRONICS_50","DISCOUNT10"], businessLine = ["grocery","electronics","invalid"], isActive = [False,True,True]))

        