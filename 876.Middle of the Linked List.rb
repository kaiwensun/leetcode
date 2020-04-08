# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} head
# @return {ListNode}
def middle_node(head)
    def walk(node, count)
        if node.nil?
            puts count / 2
            count / 2
        else
            res = walk(node.next, count + 1)
            (res.is_a? ListNode or count != res) ? res : node
        end
    end
    walk(head, 0)
end
