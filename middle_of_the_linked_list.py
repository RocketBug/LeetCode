# problem url https://leetcode.com/problems/middle-of-the-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head.next == None:
            return head
        
        ptr_ctr = 1
        ptr = head
        
        while ptr.next:
            ptr = ptr.next
            ptr_ctr += 1
            
        mid = (ptr_ctr//2)+1
        
        for i in range(mid-1):
            head = head.next            
        
        return head
        
        
        
        