# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur =  head
        nxt = None
        while cur:
            if cur.next:
                nxt = cur.next
            else:
                nxt = None
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
            