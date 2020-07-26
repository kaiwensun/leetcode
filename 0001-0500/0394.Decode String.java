/**
 *Basic idea:
 * maintain two stacks. One takes integers, another takes strings in a matched [....].
 *Result:
 * 26 / 26 test cases passed.
 * Status: Accepted
 * Runtime: 4 ms
 * Your runtime beats 40.86% of java submissions.
 *Date:
 * 10/30/2016
 */
public class Solution {
    public String decodeString(String s) {
        Stack<Integer> stackInt = new Stack<>();
        Stack<StringBuilder> stackStr = new Stack<>();
        stackStr.push(new StringBuilder());
        int i=0;
        while(i<s.length()){
            char c = s.charAt(i);
            if(c>='0' && c<='9'){
                int j = i+1;
                while(j<s.length() && s.charAt(j)>='0' && s.charAt(j)<='9')
                    j++;
                stackInt.push(Integer.parseInt(s.substring(i,j)));
                i = j-1;
            }else if(c=='['){
                stackStr.push(new StringBuilder());;
            }else if(c==']'){
                StringBuilder unit = stackStr.pop();
                int copy = stackInt.pop();
                StringBuilder sb = new StringBuilder();
                for(int j=0;j<copy;j++){
                    sb.append(unit);
                }
                stackStr.peek().append(sb);
            }else{
                stackStr.peek().append(c);
            }
            i++;
        }
        return stackStr.pop().toString();
    }
}
