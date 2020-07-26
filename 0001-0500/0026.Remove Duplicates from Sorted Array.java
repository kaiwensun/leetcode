/**
 *Result:
 * 161 / 161 test cases passed.
 * Status: Accepted
 * Runtime: 1 ms
 * Your runtime beats 54.77% of javasubmissions.
 *Date:
 * 9/1/2016
 */
public class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums==null || nums.length==0)
            return 0;
        int cnt = 0;
        int pioneer = 1;
        while(pioneer<nums.length){
            if(nums[cnt]!=nums[pioneer]){
                nums[++cnt]=nums[pioneer];
            }
            pioneer++;
        }
        return cnt+1;
    }
}
