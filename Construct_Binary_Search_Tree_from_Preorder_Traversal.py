# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    def constructBst(self, preorder, n, pos, curr, min_val, max_val):
        if pos == n or preorder[pos]<min_val or preorder[pos]>max_val:
            return pos
        
        if preorder[pos] < curr.val:
            node = TreeNode(preorder[pos])
            curr.left = node
            pos += 1
            pos = self.constructBst(preorder, n, pos, curr.left, min_val, curr.val-1)
            
        if pos == n or preorder[pos]<min_val or preorder[pos]>max_val:
            return pos
        
        node = TreeNode(preorder[pos])
        curr.right = node
        pos += 1
        pos = self.constructBst(preorder, n, pos, curr.right, curr.val+1, max_val)
        
        return pos
        
        
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        n = len(preorder)
        
        if not n:
            return None
        
        root = TreeNode(preorder[0])
        if n == 1:
            return root
        
        self.constructBst(preorder, n, 1, root, float('-inf'), float('inf'))
        return root
        