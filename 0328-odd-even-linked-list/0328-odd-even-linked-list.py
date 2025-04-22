# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        od, ev, tmp = head, head.next, head.next
        while ev and ev.next:
            od.next, ev.next = od, ev= od.next.next, ev.next.next
        od.next = tmp
        return head
