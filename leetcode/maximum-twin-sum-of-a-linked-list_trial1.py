# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        prev = None
        curr = slow
        nxt = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # Calc maxi
        maxi = 0
        left, right = head, prev
        while right:                        
            maxi = max(maxi, left.val + right.val)
            left = left.next
            right = right.next

        return maxi