#problem url https://leetcode.com/problems/majority-element/

from collections import Counter
import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        nums_len = len(nums)
        threshold = math.ceil(nums_len/2)
        
        for n in nums:
            if c[n] >= threshold:
                return n
            