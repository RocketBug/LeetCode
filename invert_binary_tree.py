#problem url https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = []
        visited = []
        queue.append(root)
        visited.append(root)
        
        if root == None:
            return root
        
        while len(queue) > 0:
            neighbours = []
            top = queue.pop(0)
            
            if top != None:
                neighbours.append(top.right)
                neighbours.append(top.left)
            
            for n in neighbours:
                if n not in visited:
                    queue.append(n)
                    visited.append(n)
            
            if len(neighbours) > 0:
                top.left = neighbours[0]
                top.right = neighbours[1]
            
        return root