import java.math.BigInteger; 

class Solution {
    private final static int MOD = 1000000007;
    public int numberOfWays(int num_people) {
        int[] dp = new int[num_people / 2 + 1];
        dp[0] = 1;
        for (int shakes = 1; shakes <= num_people / 2; shakes++) {
            int res = dp[shakes - 1];
            for (int leftSize = 0; leftSize <= shakes - 2; leftSize++) {
                for (int midSize = 0; midSize <= shakes - leftSize - 2; midSize++) {
                    int rightSize = shakes - leftSize - midSize - 2;
                    long prod = ((long)dp[leftSize] * (long)dp[midSize]) % MOD;
                    prod = ((long)prod * (long)dp[rightSize]) % MOD;
                    res = (int)((res + prod) % MOD);
                }
            }
            dp[shakes] = res;
        }
        return dp[dp.length - 1];
    }
}
