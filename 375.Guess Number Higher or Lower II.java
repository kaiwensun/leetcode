/**
 *Basic idea:
 * dynamic progrmming
 *Result:
 * 13 / 13 test cases passed.
 * Status: Accepted
 * Runtime: 10 ms
 * We are in the progress of updating the graph distribution. Please check the distribution again within weeks.
 *Date:
 * 9/8/2016
 */
public class Solution {
    public int getMoneyAmount(int n) {
        int[][] dp = new int[n+2][n+1];
        for(int len = 1;len<n;len++){
            for(int start=1;start<=n-len;start++){
                int end = start+len;
                int min = Integer.MAX_VALUE;
                for(int split = start+len/2;split<=end;split++){
                    int value = (dp[start][split-1]>dp[split+1][end]?dp[start][split-1]:dp[split+1][end])+split;
                    min = min<value?min:value;
                }
                dp[start][end] = min;
            }
        }
        return dp[1][n];
    }
}
