class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head
        for i in range(n-1):
            fast = fast.next
            
        while fast.next is not None:
            fast = fast.next
            prev = slow
            slow = slow.next
        
        if slow == head:
            head = slow.next
        else:
            prev.next = slow.next
        
        return head 
            