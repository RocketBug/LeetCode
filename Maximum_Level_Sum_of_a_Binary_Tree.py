#https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        
        q = deque([root])
        max_sum = root.val
        max_sum_level = 1
        level = 0
        
        while q:
            total = 0
            n = len(q)
            level += 1
            
            for i in range(n):
                node = q.popleft()
                total += node.val
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
                    
            if total > max_sum:
                max_sum = total
                max_sum_level = level
                
        return max_sum_level 
            
                    
                