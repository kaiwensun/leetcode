# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        def track(node):
            if not node:
                return 0
            rtn = track(node.next)
            val = node.val * 2 + rtn
            node.val = val % 10
            return val // 10
        track(dummy)
        return dummy if dummy.val else dummy.next

