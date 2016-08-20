/**
 *Result:
 * 18 / 18 test cases passed.
 * Status: Accepted
 * Runtime: 0 ms
 * Your runtime beats 9.75% of javasubmissions.
 *Date:
 * 8/20/2016
 */
public class Solution {
    public String convertToTitle(int n) {
        if(n==0)
            return "";
        return convertToTitle((n-1)/26)+(((n%26)==0)?'Z':(char)((int)'A'+(n%26)-1));
    }
}
