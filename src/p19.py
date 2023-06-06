from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

## Runtime 68.4%
## Memory 56.3%
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        h = head
        while h:
            nodes.append(h)
            h = h.next
        if len(nodes) == 1:
            return None
        if len(nodes) - n <= 0:
            return nodes[1]
        node = nodes[len(nodes) - 1 - n]
        node.next = node.next.next
        return head