class MyStack {
    private Queue<Integer> q = new LinkedList<Integer>();
    private Queue<Integer> p = new LinkedList<Integer>();

    public void push(int x) {
        q.offer(x);
    }

    public int pop() {
        if(q.isEmpty())
            return -1;
        int res = this.top();
        while(q.size()>1){
            p.offer(q.poll());
        }
        q.poll();
        Queue<Integer> tmp = p;
        p = q;
        q = tmp;
        return res;
    }

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

    public boolean empty() {
        return q.isEmpty();
    }
}
/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */

