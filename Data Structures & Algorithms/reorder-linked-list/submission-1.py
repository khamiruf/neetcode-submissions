# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle node
        # split the LL into half
        # reverse the second half of the LL
        # join the 2 LL (1st ll then 2nd ll)
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        
        l2 = None
        while second:
            tmp = second.next
            second.next = l2
            l2 = second
            second = tmp
        
        # l2 is the start of the second ll now
        first = head
        tail = head
        while first and l2:
            tmp1, tmp2 = first.next, l2.next
            first.next = l2
            l2.next = tmp1
            first = tmp1
            l2 = tmp2