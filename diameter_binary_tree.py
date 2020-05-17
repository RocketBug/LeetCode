#problem url https://leetcode.com/problems/diameter-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Answer:
    def __init__(self):
        self.ans = float('-inf')
            
class Solution:
    
    def dfs_tree(self, head, a):
        if head == None:
            return 0
        
        left_sum = Solution.dfs_tree(Solution, head.left, a)
        right_sum = Solution.dfs_tree(Solution, head.right, a)
        
        a.ans = max(a.ans, (left_sum+right_sum))
        
        return max(left_sum, right_sum)+ 1
            
        
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        a = Answer()
        self.dfs_tree(root, a)
        return a.ans