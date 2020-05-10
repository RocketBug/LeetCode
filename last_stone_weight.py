#problem url https://leetcode.com/problems/last-stone-weight/
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort()
            last_stone = stones.pop(-1)
            second_last_stone = stones.pop(-1)
            diff = last_stone - second_last_stone
            if diff:
                stones.append(diff)
                
                
        if not len(stones):
            return 0
        
        else:
            return stones[0]
                
        
        