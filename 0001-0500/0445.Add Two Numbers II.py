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
        def genNums(lst):
            if lst:
                for num in genNums(lst.next):
                    yield num
                yield lst.val
        
        gen1, gen2 = genNums(l1), genNums(l2)
        v1, v2 = next(gen1, None), next(gen2, None)
        carry = 0
        res = None
        while not (v1 is None and v2 is None and carry == 0):
            num = (v1 or 0) + (v2 or 0) + carry
            carry = num // 10
            num %= 10
            res = ListNode(num, res)
            v1, v2 = next(gen1, None), next(gen2, None)
        return res

