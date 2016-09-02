/**
 *Basic idea:
 * View Each bit independently. Count the appearance by pushing the flag bit (1) circularly from `one` to `three`.
 *Result:
 * 11 / 11 test cases passed.
 * Status: Accepted
 * Runtime: 1 ms
 * Your runtime beats 86.59% of javasubmissions.
 *Date:
 * 9/2/2016
 */
public class Solution {
    public int singleNumber(int[] nums) {
        int one = -1;
        int two = 0;
        int three = 0;
        for(int e : nums){
            int tmpthree = three;
            three = (three&~e) | (two & e);
            two = (two&~e) | (one & e);
            one = (one&~e) | (tmpthree & e);
        }
        return two;
    }
}
