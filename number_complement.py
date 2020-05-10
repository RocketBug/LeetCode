#problem url https://leetcode.com/problems/number-complement/
class Solution:
    def findComplement(self, num: int) -> int:
        i = num
        
        num |= num >> 1
        num |= num >> 2
        num |= num >> 4
        num |= num >> 8
        num |= num >> 16
        
        
        return i ^ num