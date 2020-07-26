#This is a solution from LeetCoders
#The basic idea is to sort(heapsort) the array of lists by the first element in each list. Pick the least element of the least list.
#I have thought of sort, but I didn't use the heapsort. I used listsort, which is less efficient.
#Also, Python's heapq package is useful!
def mergeKLists(self, lists):
    from heapq import heappush, heappop, heapreplace, heapify
    dummy = node = ListNode(0)
    h = [(n.val, n) for n in lists if n]
    heapify(h)
    while h:
        v, n = h[0]
        if n.next is None:
            heappop(h) #only change heap size when necessary
        else:
            heapreplace(h, (n.next.val, n.next))
        node.next = n
        node = node.next

    return dummy.next

