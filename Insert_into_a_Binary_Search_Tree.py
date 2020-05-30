
#https://leetcode.com/problems/insert-into-a-binary-search-tree/
# Definition for a binary tree node.

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    counter = 0 
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        Solution.counter += 1

        if val < root.val:
            if root.left == None:
                root.left = TreeNode(val)
                
            else:
                self.insertIntoBST(root.left, val)
                
        else:
            if root.right == None:
                root.right = TreeNode(val)
                
            else:
                self.insertIntoBST(root.right, val)
        
        Solution.counter -= 1
            
        if Solution.counter == 0:
            return root