class Solution {
    private int[] dp;
    public int change(int amount, int[] coins) {
        dp = new int[amount + 1];
        dp[0] = 1;
        for (int coin : coins) {
            for (int i = 0; i < amount; i++) {
                if (i + coin <= amount) {
                    dp[i + coin] += dp[i];
                } else {
                    break;
                }
            }
        }
        return dp[amount];
    }
}
