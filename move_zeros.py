#problem url https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        ctr = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[ctr] = nums[i]
                ctr += 1
            
        while ctr < len(nums):
            nums[ctr] = 0
            ctr+=1
                
        