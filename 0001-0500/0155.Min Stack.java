/**
 * Basic idea:
 * 	deep inside stack is invisible, current info is mentained at stack top.
 * Result:
 * 	17 / 17 test cases passed.
 * 	Status: Accepted
 * 	Runtime: 8 ms
 * 	Your runtime beats 73.97% of java submissions.
 * Date:
 * 	/2/7/2016
 */
import java.util.LinkedList;
class MinStack {
    private class Elem{
        Elem(int val,int min){
            this.val=val;
            this.min = min;
        }
        Elem(int val){
            this.val = val;
            this.min = val;
        }
        int val;
        int min;
    }
    private LinkedList<Elem> stack = new LinkedList<Elem>();
    public void push(int x) {
        if(stack.size()==0)
            stack.add(new Elem(x));
        else
            stack.add(new Elem(x,Math.min(x,stack.getLast().min)));
    }

    public void pop() {
        stack.removeLast();
    }

    public int top() {
        return stack.getLast().val;
    }

    public int getMin() {
        return stack.getLast().min;
    }
}

