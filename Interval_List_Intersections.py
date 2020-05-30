#https://leetcode.com/problems/interval-list-intersections/
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        aptr = 0
        bptr = 0
        result = []
        while aptr < len(A) and bptr < len(B):
            if A[aptr][1] >= B[bptr][0] and B[bptr][1] >= A[aptr][0]:
                result.append([max(A[aptr][0], B[bptr][0]), min(A[aptr][1], B[bptr][1])])
                
            if B[bptr][1] > A[aptr][1]:
                aptr += 1
                
            else:
                bptr += 1
                
        return result