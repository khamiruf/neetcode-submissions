# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # [1,2,3,4,5,6,7]
        dummy = ListNode(0, head)
        before, after = dummy, head
        for _ in range(n):
            after = after.next
        
        while before and after:
            before = before.next
            after = after.next

        # now, before.next is the node to be removed
        before.next = before.next.next

        return dummy.next