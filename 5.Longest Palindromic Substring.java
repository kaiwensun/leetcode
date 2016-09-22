/**
 *Basic idea:
 * Dynamic programming (Manacher algorithm. Keep record of the center and radius of the palindrom that reaches the right most position.
 * Make use of the already calculated length of sub-palindrom when the to-be-calculated center is left to that right-most position.
 * See http://blog.163.com/zhaohai_1988/blog/static/2095100852012716105847112/)
 *Result:
 * 88 / 88 test cases passed.
 * Status: Accepted
 * Runtime: 56 ms
 * Your runtime beats 40.09% of java submissions.
 *Date:
 * 9/21/2016
 */
public class Solution {
    private static final char SPLIT = '#';
    public String longestPalindrome(String s) {
        if(s.length()==0)
            return s;
        StringBuilder sb = new StringBuilder(SPLIT);
        for(int i=0;i<s.length();i++){
            sb.append(s.charAt(i));
            sb.append(SPLIT);
        }
        s = sb.toString();
        int[] p = new int[s.length()];
        p[0] = 1;
        int id = 0;
        int rb = 0;
        int maxid = 0;
        for(int i=1;i<s.length();i++){
            int j = id*2-i;
            if(i<=rb)
                p[i] = p[j];
            else
                p[i]=1;
            int l = i-1;
            int r = i+1;
            while(l>=0 && r<s.length() && s.charAt(l)==s.charAt(r)){
                l--;
                r++;
            }
            p[i] = r-i;
            if(r-1>rb){
                id = i;
                rb = rb;
            }
            if(p[maxid]<p[i]){
                maxid = i;
            }
            
        }
        return retriveSubstring(s,maxid,p[maxid]);
    }
    private String retriveSubstring(String str, int id, int radius){
        StringBuilder sb = new StringBuilder();
        for(int i=(str.charAt(id-radius+1)==SPLIT)?(id-radius+2):(id-radius+1);i<id+radius;i+=2)
            sb.append(str.charAt(i));
        return sb.toString();
    }
}
