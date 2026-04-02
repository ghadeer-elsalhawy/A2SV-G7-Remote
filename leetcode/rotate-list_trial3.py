# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # Find tail and clean rounds
        total = 1
        tail = head
        while tail and tail.next:
            total += 1
            tail = tail.next
        rotate = k % total
        if rotate == 0:
            return head
        # print(rotate)
        before = None
        n_head = head
        counter = 1
        while counter < total - rotate + 1:
            before = n_head
            n_head = n_head.next
            counter += 1
        before.next = None
        tail.next = head
        return(n_head)