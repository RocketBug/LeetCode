#https://leetcode.com/problems/counting-bits/
class Solution:
    def countBits(self, num: int) -> List[int]:
        mem = []
        mem.append(0)
        
        for i in range(1, num+1):
            val = mem[i//2] + i%2
            mem.append(val)
            
        return mem