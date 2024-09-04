# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sl, fa, pre = head,head,None
        while fa and fa.next:
            pre =sl
            sl=sl.next
            fa=fa.next.next
        if pre==None:
            return None
        pre.next = sl.next
        return head
        