from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

## Runtime 68.4%
## Memory 95.2%
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head
        while head:
            if head.next:
                head.val, head.next.val = head.next.val, head.val
                head = head.next.next
            else:
                break
        return res