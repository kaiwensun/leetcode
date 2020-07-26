/**
 *Basic idea:
 * stack
 *Result:
 * 20 / 20 test cases passed.
 * Status: Accepted
 * Runtime: 13 ms
 * Your runtime beats 94.33% of javasubmissions.
 *Date:
 * 9/8/2016
 */

public class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for(String token : tokens){
            switch(token){
                case "+":
                    stack.push(stack.pop()+stack.pop());
                    break;
                case "-":
                    stack.push(-stack.pop()+stack.pop());
                    break;
                case "*":
                    stack.push(stack.pop()*stack.pop());
                    break;
                case "/":
                    Integer a = stack.pop();
                    Integer b = stack.pop();
                    stack.push(b/a);
                    break;
                default:
                    stack.push(Integer.parseInt(token));
            }
        }
        return stack.pop();
    }
}
