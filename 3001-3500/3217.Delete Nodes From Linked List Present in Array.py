# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        prev = dummy = ListNode()
        p = head
        while p:
            if p.val not in nums:
                prev.next = p
                prev = prev.next
            p = p.next
        prev.next = None
        return dummy.next

