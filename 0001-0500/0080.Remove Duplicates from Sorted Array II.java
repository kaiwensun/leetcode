/**
 *Basic Idea:
 * compare nums[pioneer] with nums[cnt-1], rather than nums[cnt].
 *Result:
 * 164 / 164 test cases passed.
 * Status: Accepted
 * Runtime: 1 ms
 * Your runtime beats 59.44% of javasubmissions.
 *Date:
 * 9/1/2016
 */
public class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums==null || nums.length==0)
            return 0;
        if(nums.length==1)
            return 1;
        int cnt = 1;
        int pioneer = 2;
        while(pioneer<nums.length){
            if(nums[cnt-1]!=nums[pioneer]){
                nums[++cnt]=nums[pioneer];
            }
            pioneer++;
        }
        return cnt+1;
    }
}
