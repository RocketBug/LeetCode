#problem url https://leetcode.com/problems/cousins-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, val):
        depth = 0
        s = []
        level = {}
        level[root] = 0
        s.append(root)
        
        while len(s):
            top = s.pop(-1)
            if top.val == val:
                return (top, 0)
            neighbours = []
            if top.left != None:
                neighbours.append(top.left)
            if top.right != None:
                neighbours.append(top.right)
                
            for n in neighbours:
                if n.val == val:
                    return (top, level[top]+1)
                
                elif n not in level:
                    level[n] = level[top] + 1
                    s.append(n)
                

                                    
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        x_val = self.dfs(root, x)
        y_val = self.dfs(root, y)
        if x_val[0] != y_val[0] and x_val[1] == y_val[1]:
            return True
        
        else:
            return False
        
        
        
        