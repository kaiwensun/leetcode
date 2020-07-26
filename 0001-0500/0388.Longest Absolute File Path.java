/**
 *Basic idea:
 * stack
 *Result:
 * 25 / 25 test cases passed.
 * Status: Accepted
 * Runtime: 11 ms
 * Sorry. We do not have enough accepted submissions.
 *Date:
 * 9/2/2016
 */
public class Solution {
    public int lengthLongestPath(String input) {
        String[] dirs = input.split("\\n");
        Stack<Integer>stack = new Stack<>();
        int maxlen = 0;
        for(String dir : dirs){
            int level = countLevel(dir);
            int filelen = dir.length()-level;
            boolean isfile = isFile(dir);
            while(stack.size()>level){
                stack.pop();
            }
            if(isfile){
                int abslen = (stack.isEmpty()?0:stack.peek())+dir.length();
                maxlen = maxlen>abslen?maxlen:abslen;
            }
            else{
                stack.push((stack.isEmpty()?0:stack.peek())+filelen);
            }
        }
        return maxlen;
    }
    private boolean isFile(String filename){
        return filename.contains(".");
    }
    private int countLevel(String filename){
        for(int i=0;i<filename.length();i++){
            if(filename.charAt(i)!='\t')
                return i;
        }
        return 0;
    }
}
