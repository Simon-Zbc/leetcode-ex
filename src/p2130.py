from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## Runtime 32.7%
## Memory 13.9%
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur = head
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next
        res, n = 0, len(arr)
        for i in range(n):
            res = max(res, arr[i] + arr[n-i-1])
        return res