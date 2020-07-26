/**
 *Result:
 * 15 / 15 test cases passed.
 * Status: Accepted
 * Runtime: 1 ms
 *Date:
 * 9/6/2016
 */
public class Solution {
    public int singleNumber(int[] nums) {
        int sum = 0;
        for(int e:nums)
            sum ^= e;
        return sum;
    }
}
