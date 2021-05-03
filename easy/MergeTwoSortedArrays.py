# https://leetcode.com/problems/merge-two-sorted-lists/
# Runtime: 28 ms, faster than 97.72% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14.4 MB, less than 31.59% of Python3 online submissions for Merge Two Sorted Lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:        
        # one of the lists is empty
        if (l1 is None) and (l2 is None):
            return None 
        elif l2 is None:
            return l1
        elif l1 is None:
            return l2
    
        # neither list is empty
        # Look at first item 
        if l1.val < l2.val:
            new_list_head = l1
            l1 = l1.next
        else: 
            new_list_head = l2
            l2 = l2.next
        
        new_list = new_list_head
        while (l1 is not None) and (l2 is not None):
            if l1.val < l2.val:
                new_list.next = l1
                l1 = l1.next
            else: 
                new_list.next = l2
                l2 = l2.next
            new_list = new_list.next
            
        # one list is not complete
        if l1 is None:
            new_list.next = l2
        if l2 is None:
            new_list.next = l1 
        
        return new_list_head