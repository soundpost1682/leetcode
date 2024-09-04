# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head.next
        f , s = head.next.next, head
        while f and f.next:
            s = s.next
            f = f.next.next
        s.next = s.next.next
        return head
