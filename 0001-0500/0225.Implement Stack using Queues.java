/**
 *Result:
 * 16 / 16 test cases passed.
 * Status: Accepted
 * Runtime: 99 ms
 * Your runtime beats 63.13% of java submissions.
 *Date:
 * 10/1/2016
 */
class MyStack {
    Queue<Integer> q = new LinkedList<Integer>();
    Queue<Integer> p = new LinkedList<Integer>();
    // Push element x onto stack.
    public void push(int x) {
        q.offer(x);
    }

    // Removes the element on top of the stack.
    public void pop() {
        if(q.isEmpty())
            return;
        while(q.size()>1){
            p.offer(q.poll());
        }
        q.poll();
        Queue<Integer> tmp = p;
        p = q;
        q = tmp;
    }

    // Get the top element.
    public int top() {
        if(q.isEmpty())
            return 0;
        while(q.size()>1){
            p.offer(q.poll());
        }
        int rtn = q.poll();
        p.offer(rtn);
        Queue<Integer> tmp = p;
        p = q;
        q = tmp;
        return rtn;
    }

    // Return whether the stack is empty.
    public boolean empty() {
        return q.isEmpty();
    }
}
