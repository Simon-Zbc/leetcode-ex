from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## Runtime 6.5%
## Memory 13.4%
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        cur = head
        l = 1
        while cur.next:
            cur = cur.next
            l += 1
        cur.next = head
        k = l - (k % l)
        while k > 0:
            cur = cur.next
            k -= 1
        res = cur.next
        cur.next = None
        return res