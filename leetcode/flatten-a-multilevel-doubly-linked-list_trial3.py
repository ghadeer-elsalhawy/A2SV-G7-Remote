"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        dummy = head

        def dfs(dummy):
            if not dummy.next and not dummy.child:
                return dummy
            has_child = dummy.child
            if has_child:
                nxt = dummy.next
                child_tail = dfs(dummy.child)
                dummy.next = dummy.child
                dummy.child.prev = dummy
                dummy.child = None
                child_tail.next = nxt
                if nxt:
                    nxt.prev = child_tail
            
            return dfs(dummy.next)
                

        dfs(dummy)
        return head