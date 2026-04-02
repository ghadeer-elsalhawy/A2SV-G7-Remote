# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = head
        while dummy and dummy.next:
            # print(dummy)
            if dummy.next.val == val:
                # print("Yes")
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
        if head and head.val == val:
            return head.next
        return head