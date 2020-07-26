/**
 *Basic idea:
 * The idea is borrowed from [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/).
 * Scan the array of digits from left to right. We sill push some of them into a stack.
 * During the scan, pop elements until the current digit is not less than the top of stack. The poped digits are those removed digits.
 * Then push the current digit to the stack.
 * The essence is that when you find a digit greater than already scanned digit(s), and if you can still remove some digit(s),
 * you know you can remove those greater digits in order to make the final number smaller. After all, the length of
 * the final number is deterministic.
 * Note that:
 * - The digits in the stack are always in (non-strictly) increasing order.
 * - Do not remove more than k digits. Stop the scan when necessary.
 * - In my code, I push the index of digits rather than the digits themselves into the stack.
 *Result:
 * 30 / 30 test cases passed.
 * Status: Accepted
 * Runtime: 13 ms
 * Your runtime beats 75.54% of java submissions.
 *Date:
 * 10/4/2016
 */
public class Solution {
    public String removeKdigits(String num, int k){
        if(num==null || num.length()<=k){
            return "0";
        }
        int toBeRm = k;
        Stack<Integer> stack = new Stack<>();
        for(int i=0;i<num.length() && toBeRm>0;i++){
            while(toBeRm>0 && !stack.isEmpty() && num.charAt(i)<num.charAt(stack.peek())){
                    int r = stack.pop();
                    toBeRm--;
            }
            stack.push(i);
        }
        StringBuilder sb = new StringBuilder();
        int i=0;
        for(int index : stack){
            if(i>=num.length()-k)
                break;
            sb.append(num.charAt(index));
            i++;
        }
        if(stack.size()<num.length()-k){
            sb.append(num.substring(k+stack.size()));
        }
        String res = sb.toString();
        return trimLeadingZero(res);
    }
    private String trimLeadingZero(String num){
        for(int i=0;i<num.length();i++){
            if(num.charAt(i)!='0'){
                return num.substring(i);
            }
        }
        return "0";
    }
}
