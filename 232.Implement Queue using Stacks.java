/**
 * Basic idea:
 * 	use a backup stack when you want to access stack bottom.
 * Result:
 * 	17 / 17 test cases passed.
 * 	Status: Accepted
 * 	Runtime: 101 ms
 * 	Your runtime beats 92.62% of java submissions.
 * Date:
 * 	2/7/2016
 */
import java.util.Stack;
class MyQueue {
    private Stack<Integer> stack = new Stack<Integer>();
    private Stack<Integer> backup = new Stack<Integer>();
    
    // Push element x to the back of queue.
    public void push(int x) {
        stack.push(x);
    }

    // Removes the element from in front of queue.
    public void pop() {
        dump(stack,backup);
        backup.pop();
        dump(backup,stack);
    }

    // Get the front element.
    public int peek() {
        dump(stack,backup);
        int rtn = backup.peek();
        dump(backup,stack);
        return rtn;
    }

    // Return whether the queue is empty.
    public boolean empty() {
        return stack.empty();
    }
    
    //dump all elements from src to dst
    private void dump(Stack<Integer> src,Stack<Integer> dst){
        while(!src.empty())
            dst.push(src.pop());
    }
}

