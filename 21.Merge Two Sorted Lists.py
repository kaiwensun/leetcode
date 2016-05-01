from pdb import *
# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		if l1==None:
			return l2
		if l2==None:
			return l1
		ptr1=l1
		ptr2=l2
		head = ListNode(None)
		ptr = head
		ptr.next=ptr1
		was1=True
		#set_trace()
		while ptr1!=None and ptr2!=None:
			if ptr1.val<=ptr2.val:
				if was1==False:
					ptr.next=ptr1
					was1=True
				ptr1=ptr1.next
			else:
				if was1==True:
					ptr.next=ptr2
					was1=False
				ptr2=ptr2.next
			ptr=ptr.next
		if ptr1!=None:
			ptr.next=ptr1
		elif ptr2!=None:
			ptr.next=ptr2
		return head.next

l1=ListNode(5);
l2=ListNode(1);l2.next=ListNode(2);l2.next.next=ListNode(4)
s = Solution()
p = s.mergeTwoLists(l1,l2)
while p!=None:
	print p.val," ",
	p=p.next
print ""

