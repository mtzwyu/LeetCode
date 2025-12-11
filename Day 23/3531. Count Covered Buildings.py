class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # min_y_row[x] lưu giá trị y nhỏ nhất của hàng x
        min_y_row = [float('inf')] * (n + 1)
        max_y_row = [float('-inf')] * (n + 1)
        
        # min_x_col[y] lưu giá trị x nhỏ nhất của cột y
        min_x_col = [float('inf')] * (n + 1)
        max_x_col = [float('-inf')] * (n + 1)
        
        for x ,y in buildings:
            if y < min_y_row[x]: min_y_row[x] = y
            if y > max_y_row[x]: max_y_row[x] = y
            if x < min_x_col[y]: min_x_col[y] = x
            if x > max_x_col[y]: max_x_col[y] = x
        count = 0
        for x, y in buildings:
            
            has_horizontal = (min_y_row[x] < y < max_y_row[x])
            has_vertical = (min_x_col[y] < x < max_x_col[y])

            if has_horizontal and has_vertical:
                count +=1
        return count