# problem url https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        numsdict = {}
        resultArr = []
        for i in nums:
            if i not in numsdict:
                numsdict[i] = i
                
        
        for i in range(1, len(nums)+1):
            if i not in numsdict:
                resultArr.append(i)
                
        return resultArr