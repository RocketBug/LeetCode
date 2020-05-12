# problem url https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3327/
# similar to single_number.py

# The solution below is based on the same logic as single_number.py
# but it does not meet the time complexity of O(logN)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i = 0
        for j in nums:
            i = j^i
    
        return i

# The solution below is based on mathematics
# but this solution is also not O(logN)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return sum(set(nums))*2-sum(nums)

# The solution below is based on binary search and is O(logN)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while True:
            mid = (low + high) // 2
            if mid % 2 == 1:
                mid -= 1
            if mid < high and nums[mid] == nums[mid+1]:
                low = mid + 2
            elif mid > low and nums[mid] == nums[mid-1]:
                high = mid - 2
            else:
                return nums[mid]

