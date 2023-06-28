from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## Runtime 92.6%
## Memory 89.9%
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        temp = head
        res = pre = ListNode()
        while temp and temp.next:
            if temp.val == temp.next.val:
                temp = temp.next
                pre.next = temp
            else:
                pre.next = temp
                pre = pre.next
                temp = temp.next
        return res.next