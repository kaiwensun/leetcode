class Solution {
    public int numTilings(int N) {
        if (N <= 2){
            return N;
        }
        int MOD = 1000000007;
        int[][] dp = new int[2][];
        dp[0] = new int[]{1, 0}; // flat, non-flat
        dp[1] = new int[]{2, 1};
        for (int i = 2; i < N; ++i) {
            int oneBefore = (~i) & 1;
            int twoBefore = i & 1;
            int flat = (dp[twoBefore][0] + dp[oneBefore][0]) % MOD + (dp[oneBefore][1] * 2) % MOD;
            int nonflat = dp[oneBefore][1] + dp[twoBefore][0];
            dp[twoBefore][0] = flat % MOD;
            dp[twoBefore][1] = nonflat % MOD;
        }
        return dp[(N + 1) % 2][0];
    }
}

