class Solution:
    def countCollisions(self, directions: str) -> int:
        directions = directions.lstrip('L').rstrip('R')
        return len(directions) - directions.count('S')



class Solution1:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        l = 0
        r = n - 1
        
        while l < n and directions[l] == 'L':
            l += 1
        while r > 0 and directions[r] == 'R':
            r += 1
        
        count = 0
        for i in range(l, r+1):
            if directions[i] == 'S':
                continue
            count +=1
        return count
    
class Solution2:
    def countCollisions(self, directions: str) -> int:
        stack = []
        collisions = 0
        
        for car in directions:
            # th 1: Xe di sang phai
            if car == "R":
                stack.append(car)
            # th 2: Xe dung yen
            elif car == "S":
                # Nếu trong stack có xe đang lao tới (R), chúng sẽ đâm vào S này
                while stack and stack[-1] == 'R':
                    stack.pop()
                    collisions += 1
                stack.append(car)
            # th 3: Xe di sang trai
            elif car == 'L':
                if stack and stack[-1] == 'S':
                # L đâm vào xe đứng yên bên trái
                    collisions +=1
                # Xe L dừng lại, vẫn coi là vật cản S (đã có S trong stack rồi nên ko cần push thêm)
                elif stack and stack[-1] == 'R':
                # L đâm trực diện xe R
                    collisions += 2
                    stack.pop() # Xe R dừng lại
                    # Sau va chạm, tạo thành vật cản, kiểm tra xem có xe R nào phía sau đâm tiếp không
                    while stack and stack[-1] == 'R':
                        collisions += 1
                        stack.pop()
                    stack.append('S') # Lưu lại xác xe
        return collisions