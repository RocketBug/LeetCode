# leetcode may challenge day 30

class Solution:
    
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        
        def euclid(p):
            return p[0]**2 + p[1]**2
    
        return sorted(points, key = euclid)[0:K]