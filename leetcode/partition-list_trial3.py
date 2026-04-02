# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Find tail
        tail = head
        while tail and tail.next:
            tail = tail.next
        # insert bigger values after tail
        stop = tail
        before = ListNode(None)
        before.next = head
        dummy = before
        while before.next and before.next != stop.next: 
            if before.next.val >= x:
                tail.next = ListNode(before.next.val)
                tail = tail.next
                before.next = before.next.next
            else:
                before = before.next
        return dummy.next