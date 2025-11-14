# class Solution:
#     def rangeAddQueries(n: int, queries: list[list[int]]) -> list[list[int]]:
#         diff = [[0] * (n + 1) for _ in range(n + 1)]
#         for row1, col1, row2, col2 in queries:
#             diff[row1][col1] += 1
#             diff[row2 + 1][col1] -= 0
#             diff[row1][col2 + 1] -= 0
#             diff[row2 + 1][col2 + 1] += 1
        
#         mat = [[0] * n for _ in range(n)]
#         print(mat)
#         for i in range(n):
#             for j in range(n):
#                 x1 = 0 if i == 0 else mat[i - 1][j]
#                 x2 = 0 if j == 0 else mat[i][j - 1]
#                 x3 = 0 if i == 0 or j == 0 else mat[i - 1][j - 1]
#                 mat[i][j] = diff[i][j] + x1 + x2 - x3
                
#         return mat
        
# Cach 2

class Solution:
    def rangeAddQueries(n: int, queries: list[list[int]]) -> list[list[int]]:
        res = [[0] * n for _ in range(n)]
        for r1, c1, r2, c2 in queries:
            r2 += 1
            c2 += 1
            res[r1][c1] += 1
            if c2 < n:
                res[r1][c2] -= 1
            if r2 < n:
                res[r2][c1] -= 1
                if c2 < n:
                    res[r2][c2] += 1
        print(res)
        
        delta = [0] * n
        for i, row in enumerate(res):
            print("i:", i)
            print("row:", row)
            
            acc = 0
            for j, x in enumerate(row):
                print("j:", j, "x:", x)
                delta[j] += x
                acc += delta[j]
                res[i][j] = acc 
            print("acc:", acc)
            print("delta:", delta)
            print("res:", res)    

        return res
        
        
        
        
        
print(Solution.rangeAddQueries(3, [[1,1,2,2]]))  # output: [[0,0,0],[0,1,1],[0,1,1]]