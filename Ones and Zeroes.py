class Solution:
    def findMaxFrom(strs: list[str], m: int, n: int):
        dp = {(0,0): 0}

        for s in strs:
            ones = 0
            zeroes = 0
            for ch in s:
                if ch == '0':
                    zeroes +=1
                else:
                    ones +=1
            newdp = {}

            for k,v in dp.items():
                prevzeroes, prevones = k
                newzeroes, newones = prevzeroes + zeroes, prevones + ones
                if newzeroes <= m and newones <= n:
                    if (newzeroes, newones) not in dp :
                        newdp[(newzeroes, newones) ] = v +1

                    elif dp[(newzeroes, newones)] < v +1:
                        newdp[(newzeroes, newones) ] = v +1
            dp.update(newdp)
        return max(dp.values())

        
print(Solution.findMaxFrom(["10","0001","111001","1","0"], 4, 3))  # Output: 3
