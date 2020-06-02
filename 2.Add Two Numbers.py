# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def nextOrDefault(ptr):
            if ptr:
                res = ptr.val
                ptr = ptr.next
            else:
                res = 0
            return res, ptr
        carry = 0
        ptr = head = ListNode(0)
        while l1 or l2 or carry:
            add1, l1 = nextOrDefault(l1)
            add2, l2 = nextOrDefault(l2)
            sm = add1 + add2 + carry
            ptr.next = ListNode(sm % 10)
            ptr = ptr.next
            carry = sm / 10
        return head.next or head
