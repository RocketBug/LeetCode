#problem url https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        next_node = None
        curr = head
        while curr != None:
            next_node = curr.next 
            curr.next = prev
            prev = curr
            curr = next_node
            
        return prev