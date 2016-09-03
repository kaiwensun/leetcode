/**
 *Basic idea:
 * Dynamic Programming
 *Result:
 * 17 / 17 test cases passed.
 * Status: Accepted
 * Runtime: 5 ms
 * Sorry. We do not have enough accepted submissions.
 *Date:
 * 9/3/2016
 */
public class Solution {
    public int combinationSum4(int[] nums, int target) {
        int[] dp = new int[target+1];
        dp[0]=1;
        for(int i=1;i<=target;i++){
            for(int e:nums){
                if(i-e>=0)
                    dp[i]+=dp[i-e];
            }
        }
        return dp[target];
    }
}
