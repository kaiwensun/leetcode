/**
 *Result:
 * 14 / 14 test cases passed.
 * Status: Accepted
 * Runtime: 1 ms
 * Your runtime beats 17.25% of javasubmissions.
 *Date:
 * 8/20/2016
 */
public class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        if(nums==null || nums.length==0 || s==0)
            return 0;
        int l = 0;
        int r = 0;
        int minlen = nums.length+1;
        int sum = 0;
        while(r<nums.length){
            sum += nums[r];
            r++;
            while(l<r && sum-nums[l]>=s){
                sum -= nums[l];
                l++;
            }
            if(sum>=s)
                minlen = r-l<minlen?r-l:minlen;
        }
        if(minlen==nums.length+1)
            return 0;
        return minlen;
    }
}
