/**
 * Basic idea:
 * 	carry=26.
 * Result:
 *	1000 / 1000 test cases passed.
 *	Status: Accepted
 *	Runtime: 3 ms
 *	Your runtime beats 11.60% of java submissions.
 * Date:
 * 	2/7/2016
 */
public class Solution {
    public int titleToNumber(String s) {
        int num = 0;
        for(int i=0;i<s.length();i++)
            num=num*26+s.charAt(i)-'A'+1;
        return num;
    }
}

