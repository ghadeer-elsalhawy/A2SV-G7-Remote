# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        dummy = head
        n = 0
        while dummy:
            n += 1
            dummy = dummy.next
        # section size 
        rem = n % k
        size = n // k
        res = []
        dummy = head
        sec = ListNode(0)
        d = sec
        cur = 0
        while len(res) < k:
            if cur == size:
                if rem:
                    rem -= 1
                    d.next = ListNode(dummy.val)
                    d = d.next
                    dummy = dummy.next
                res.append(sec.next)
                sec = ListNode(0)
                d = sec
                cur = 0
            else:
                d.next = ListNode(dummy.val)
                cur += 1
                dummy = dummy.next
                d = d.next
        return res