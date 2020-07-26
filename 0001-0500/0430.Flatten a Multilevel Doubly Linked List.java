/*
// Definition for a Node.
class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;
};
*/

class Solution {
    public Node flatten(Node head) {
        flattenAndGetTail(head);
        return head;
    }
    
    private Node flattenAndGetTail(Node head) {
        Node p = new Node();
        p.next = head;
        while (p.next != null) {
            p = p.next;
            if (p.child != null) {
                Node next = p.next;
                Node childTail = flattenAndGetTail(p.child);
                p.next = p.child;
                p.child.prev = p;
                childTail.next = next;
                if (next != null) {
                    next.prev = childTail;
                }
                p.child = null;
            }
        }
        return p;
    }
}
