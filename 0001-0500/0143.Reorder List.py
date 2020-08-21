# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        p = head
        lst = []
        while p:
            lst.append(p)
            p = p.next
        i, j = 0, len(lst) - 1
        while i <= j:
            lst[i].next = lst[j]
            lst[j].next = lst[i + 1]
            i += 1
            j -= 1
        lst[j + 1].next = None
        return lst[0]

