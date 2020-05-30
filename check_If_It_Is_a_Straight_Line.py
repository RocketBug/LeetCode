#problem url https://leetcode.com/problems/check-if-it-is-a-straight-line/
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        pointOne = coordinates[0]
        pointTwo = coordinates[1]
        
        result = True
        
        if pointOne[0] != pointTwo[0]:
            m = (pointOne[1] - pointTwo[1]) / (pointOne[0] - pointTwo[0])
        
            y_inter = (-m*pointOne[0]) + pointOne[1]
        
            for p in coordinates[2:]:
                y = (m*p[0]) + y_inter
                if p[1] != y:
                    return False
            
        else:
            x_inter = pointOne[0]
            for p in coordinates[2:]:
                if x_inter != p[0]:
                    return False
                
        return result