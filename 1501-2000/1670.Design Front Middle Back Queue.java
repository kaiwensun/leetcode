import java.util.ArrayDeque;
import java.util.Deque;

class FrontMiddleBackQueue {
    private Deque<Integer> left;
    private Deque<Integer> right;

    public FrontMiddleBackQueue() {
        left = new ArrayDeque<>();
        right = new ArrayDeque<>();
    }
    
    public void pushFront(int val) {
        left.addFirst(val);
        rebalance();
    }
    
    public void pushMiddle(int val) {
        left.addLast(val);
        rebalance();
    }
    
    public void pushBack(int val) {
        right.addLast(val);
        rebalance();
    }
    
    public int popFront() {
        Integer res = left.isEmpty() ? right.pollFirst() : left.removeFirst();
        if (res == null) {
            return -1;
        }
        rebalance();
        return res;
    }
    
    public int popMiddle() {
        Integer res;
        res = left.size() < right.size() ? right.removeFirst() : left.pollLast();
        if (res == null) {
            return -1;
        }
        rebalance();
        return res;
    }
    
    public int popBack() {
        Integer res = right.pollLast();
        if (res == null) {
            return -1;
        }
        rebalance();
        return res;
    }

    private void rebalance() {
        int half = (left.size() + right.size()) / 2;
        if (left.size() < half) {
            left.add(right.removeFirst());
        } else if (left.size() > half) {
            right.addFirst(left.removeLast());
        }
    }
}

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * FrontMiddleBackQueue obj = new FrontMiddleBackQueue();
 * obj.pushFront(val);
 * obj.pushMiddle(val);
 * obj.pushBack(val);
 * int param_4 = obj.popFront();
 * int param_5 = obj.popMiddle();
 * int param_6 = obj.popBack();
 */

