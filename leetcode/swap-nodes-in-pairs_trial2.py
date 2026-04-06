# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        first = head
        second = head.next
        before = ListNode(0)
        dummy = before
        while first and second:
            rest = second.next
            first.next = rest
            second.next = first
            dummy.next = second
            # print(first, "\n", second, "\n", rest)
            if first.next and first.next.next:
                dummy = first
                # print("here")
                first = first.next
                second = first.next
            else:
                break
        return before.next