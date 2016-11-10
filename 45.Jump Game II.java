/**
 *Basic idea:
 * For step k, suppose we've known we could reach `prevFarthest`.
 * For step k+1, search i=(farthest of (k-1), prevFarthest] to find the `farthest` of step k+1.
 *Result:
 * 91 / 91 test cases passed.
 * Status: Accepted
 * Runtime: 9 ms
 * Your runtime beats 90.53% of java submissions.
 *Date:
 * 11/9/2016
 */
public class Solution {
    public int jump(int[] nums) {
        int step = 0;
        int prevFarthest = 0;
        int farthest = 0;
        for(int i=0;i<nums.length;i++){
            if(i>prevFarthest){
                prevFarthest = farthest;
                step++;
            }
            farthest = farthest>i+nums[i]?farthest:(i+nums[i]);
        }
        return step;
    }
}
