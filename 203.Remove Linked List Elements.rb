# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} head
# @param {Integer} val
# @return {ListNode}
def remove_elements(head, val)
    dummy = ListNode.new(-1, head)
    slow = dummy
    fast = head
    while fast
        fast = fast.next while fast && fast.val == val
        if fast
            slow.next.val = fast.val
            fast = fast.next
            slow = slow.next
        end
    end
    slow.next = nil
    return dummy.next
end
