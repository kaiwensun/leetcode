# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} head
# @return {ListNode}
def odd_even_list(head)
    podd = odd = ListNode.new(-1)
    peven = even = ListNode.new(-1)
    for i in (1..(1.0/0))
        break if head.nil?
        if i % 2 == 1
            podd.next = head
            podd = podd.next
        else
            peven.next = head
            peven = peven.next
        end
        head = head.next
    end
    podd.next = even.next
    peven.next = nil
    odd.next
end
