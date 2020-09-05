class Solution {
    public boolean PredictTheWinner(int[] nums) {
        int[] dp = new int[nums.length];
        System.arraycopy(nums, 0, dp, 0, nums.length);
        for (int length = 2; length <= dp.length; length++) {
            for (int start = 0; start < dp.length - length + 1; start++) {
                dp[start] = Math.max(nums[start] - dp[start + 1], nums[start + length - 1] - dp[start]);
            }
        }
        return dp[0] >= 0;
    }
}
