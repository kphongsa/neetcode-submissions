class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #find row
        l, r = 0, len(matrix) - 1

        while r >= l : 
            row = (r + l) // 2
            
            if target == matrix[row][0]:
                return True
            elif (target < matrix[row][0]):
                r = row - 1
            else:
                l = row + 1

        print(l)
        row = l - 1

        if row < 0:
            return False     
        l, r = 0, len(matrix[0]) - 1

        while r >= l : 
            col = (r + l) // 2
            print(row, col, matrix[row][col])
            
            if target == matrix[row][col]:
                return True
            elif (target < matrix[row][col]):
                r = col - 1
            else:
                l = col + 1

        return False