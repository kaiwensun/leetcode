/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        if (root != null) {
            Node starter = root;
            while (starter.left != null) {
                Node upper = starter;
                Node lower = starter.left;
                while(upper != null) {
                    lower.next = upper.right;
                    upper = upper.next;
                    if (upper != null) {
                        lower.next.next = upper.left;
                        lower = upper.left;
                    }
                }
                starter = starter.left;
            }
        }
        return root;
    }
}
