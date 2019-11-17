// Improvement than v1: after spliting out leftSize, we dont have to split the rest into midSize and rightSize. The prod of dp[midSize] and dp[rightSize] is already found by dp.

import java.math.BigInteger; 

class Solution {
    private final static int MOD = 1000000007;
    public int numberOfWays(int num_people) {
        int[] dp = new int[num_people / 2 + 1];
        dp[0] = 1;
        for (int shakes = 1; shakes <= num_people / 2; shakes++) {
            int res = dp[shakes - 1];
            for (int leftSize = 0; leftSize <= shakes - 2; leftSize++) {
                int rightSize = shakes - leftSize - 1;
                res += ((long)dp[leftSize] * (long)dp[rightSize]) % MOD;
                res %= MOD;
            }
            dp[shakes] = res;
        }
        return dp[dp.length - 1];
    }
}
