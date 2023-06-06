from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

## Runtime 65.9%
## Memory 65.7%
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        resHead = tempHead = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tempHead.next = list1
                list1 = list1.next
            else:
                tempHead.next = list2
                list2 = list2.next
            tempHead = tempHead.next
        if list1:
            tempHead.next = list1
        if list2:
            tempHead.next = list2
        return resHead.next