/**
 *Basc idea:
 * dynamic programming
 *Result:
 * 69 / 69 test cases passed.
 * Status: Accepted
 * Runtime: 0 ms
 * Your runtime beats 41.45% of javasubmissions.
 *Date:
 * 9/6/2016
 */
public class Solution {
    public int rob(int[] nums) {
        if(nums==null || nums.length==0)
            return 0;
        int[] rob = new int[nums.length];
        int[] nrob = new int[nums.length];
        rob[0] = nums[0];
        for(int i=1;i<nums.length;i++){
            rob[i] = nrob[i-1]+nums[i];
            nrob[i] = rob[i-1]>nrob[i-1]?rob[i-1]:nrob[i-1];
        }
        return rob[nums.length-1]>nrob[nums.length-1]?rob[nums.length-1]:nrob[nums.length-1];
    }
}
