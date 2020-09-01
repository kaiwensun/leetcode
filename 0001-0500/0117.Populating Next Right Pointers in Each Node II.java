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

public class Solution {
    public Node connect(Node root) {
        Node starter = root;
        while(starter != null) {
            Node layerScanner = starter;
            while (layerScanner != null) {
                if (layerScanner.left != null && layerScanner.right != null) {
                    layerScanner.left.next = layerScanner.right;
                }
                Node child = layerScanner.right == null ? layerScanner.left : layerScanner.right;
                layerScanner = getChildsNextsParent(layerScanner);
                if (child != null && layerScanner != null) {
                    child.next = layerScanner.left != null? layerScanner.left : layerScanner.right;
                }
            }
            if (starter.left != null) {
                starter = starter.left;
            } else if (starter.right != null) {
                starter = starter.right;
            } else {
                Node starterParent = getChildsNextsParent(starter);
                if (starterParent != null) {
                    starter = starterParent.left == null ? starterParent.right : starterParent.left;
                } else {
                    starter = null;
                }
            }
        }
        return root;
    }
    private Node getChildsNextsParent(Node parent) {
        while (parent.next != null) {
            parent = parent.next;
            if (parent.left != null || parent.right != null) {
                return parent;
            }
        }
        return null;
    }
}
