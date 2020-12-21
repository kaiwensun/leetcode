class AllOne {

    private class ListNode {
        public Set<String> keys = new HashSet<>();
        public ListNode prev = null;
        public ListNode next = null;
        public int value;

        public ListNode(int value) {
            this.value = value;
        }
        public ListNode inc(String key) {
            if (this.next == null) {
                this.next = new ListNode(this.value + 1);
                this.next.prev = this;
            }
            if (this.next.value != this.value + 1) {
                ListNode nextnext = this.next;
                this.next = new ListNode(this.value + 1);
                this.next.prev = this;
                this.next.next = nextnext;
                nextnext.prev = this.next;
            }
            this.next.keys.add(key);
            this.keys.remove(key);
            if (this.keys.isEmpty()) {
                this.next.prev = this.prev;
                if (this.prev != null) {
                    this.prev.next = this.next;
                }
            }
            return this.next;
        }

        public ListNode dec(String key) {
            if (this.prev == null) {
                this.prev = new ListNode(this.value - 1);
                this.prev.next = this;
            }
            if (this.prev.value != this.value - 1) {
                ListNode prevprev = this.prev;
                this.prev = new ListNode(this.value - 1);
                this.prev.next = this;
                this.prev.prev = prevprev;
                prevprev.next = this.prev;
            }
            this.prev.keys.add(key);
            this.keys.remove(key);
            if (this.keys.isEmpty()) {
                this.prev.next = this.next;
                if (this.next != null) {
                    this.next.prev = this.prev;
                }
            }
            ListNode prev = this.prev;
            if (prev.value == 0 && prev.next != null) {
                prev.next.prev = null;
            }
            return prev;
        }
    }

    // private Map<String, Integer> key2value;
    private Map<String, ListNode> key2node;
    private ListNode head = null;
    private ListNode tail = null;

    /** Initialize your data structure here. */
    public AllOne() {
        key2node = new HashMap<>();
    }

    /** Inserts a new key <Key> with value 1. Or increments an existing key by 1. */
    public void inc(String key) {
        if (head == null) {
            head = tail = new ListNode(1);
            head.keys.add(key);
            key2node.put(key, head);
        } else {
            if (!key2node.containsKey(key)) {
                ListNode newHead = new ListNode(0);
                newHead.keys.add(key);
                newHead.next = head;
                head.prev = newHead;
                key2node.put(key, newHead);
                head = newHead;
            }
            ListNode oldNode = key2node.get(key);
            ListNode newNode = oldNode.inc(key);
            if (newNode.prev == null) {
                head = newNode;
            }
            if (newNode.next == null) {
                tail = newNode;
            }
            key2node.put(key, newNode);
        }
    }

    /** Decrements an existing key by 1. If Key's value is 1, remove it from the data structure. */
    public void dec(String key) {
        ListNode oldNode = key2node.get(key);
        if (oldNode == null) {
            return ;
        }
        ListNode newNode = oldNode.dec(key);
        if (newNode.value == 0) {
            head = newNode.next;
            if (head == null) {
                tail = null;
            }
            key2node.remove(key);
        } else {
            if (newNode.prev == null) {
                head = newNode;
            }
            if (newNode.next == null) {
                tail = newNode;
            }
            key2node.put(key, newNode);
        }
    }

    /** Returns one of the keys with maximal value. */
    public String getMaxKey() {
        if (tail == null) {
            return "";
        }
        return tail.keys.iterator().next();
    }

    /** Returns one of the keys with Minimal value. */
    public String getMinKey() {
        if (head == null) {
            return "";
        }
        return head.keys.iterator().next();
    }
}

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne obj = new AllOne();
 * obj.inc(key);
 * obj.dec(key);
 * String param_3 = obj.getMaxKey();
 * String param_4 = obj.getMinKey();
 */

