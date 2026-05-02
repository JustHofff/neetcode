class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        end = len(matrix[0]) - 1

        for i in range(len(matrix)):
            if matrix[i][end] == target:
                return True
            elif matrix[i][end] > target:
                while end > 0:
                    end -= 1
                    if matrix[i][end] == target:
                        return True
                return False
        
        return False