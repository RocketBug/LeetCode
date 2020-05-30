#problem url https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if l1 == None:
            return l2
        elif l2 == None:
            return l1

        dummyNode = ListNode(99)
        curr = dummyNode
        start = dummyNode
        
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
                
            curr = curr.next
        
        if l1 == None:
            curr.next = l2
        else:
            curr.next = l1
        
        start = start.next
        return start
