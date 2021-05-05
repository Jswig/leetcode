# Anders Poirel

# https://leetcode.com/problems/add-two-numbers/
# Runtime: 76 ms, faster than 30.61% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Add Two Numb

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dummy_head = ListNode(0)
        carry = 0
        curr = dummy_head
        while (l1 is not None) or (l2 is not None):
            x = l1.val if (l1 is not None) else 0
            y = l2.val if (l2 is not None) else 0
            res = x + y + carry
            carry = res // 10
            curr.next = ListNode(res % 10)
            curr = curr.next
            
            l1 = l1.next if (l1 is not None) else None
            l2 = l2.next if (l2 is not None) else None
        if carry != 0:
            curr.next = ListNode(carry)

        return dummy_head.next