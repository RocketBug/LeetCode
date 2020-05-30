# https://leetcode.com/problems/count-square-submatrices-with-all-ones/
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        
        mat = [[0 for i in range(m+1)] for j in range(n+1)]
        result = 0
    
        for i in range(1, n+1):
            for j in range(1, m+1):
                if matrix[i-1][j-1]:
                    mat[i][j] = min(mat[i-1][j], mat[i][j-1], mat[i-1][j-1]) + matrix[i-1][j-1]
                    result += mat[i][j]
        
            
        return result