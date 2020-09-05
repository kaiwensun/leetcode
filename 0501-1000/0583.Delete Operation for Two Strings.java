class Solution {
    public int minDistance(String word1, String word2) {
        if (word1.length() == 0 || word2.length() == 0) {
            return word1.length() + word2.length();
        }
        if (word1.length() > word2.length()) {
            String tmp = word1;
            word1 = word2;
            word2 = tmp;
        }
        int[] dp = new int[word2.length() + 1];
        for (int i2 = 0; i2 <= word2.length(); ++i2) {
            dp[i2] = i2;
        }
        for (int i1 = 0; i1 < word1.length(); ++i1) {
            char c1 = word1.charAt(i1);
            int oldLeftVal = i1;
            dp[0] = i1 + 1;
            for (int i2 = 0; i2 < word2.length(); ++i2) {
                int minVal = Math.min(dp[i2], dp[i2 + 1]) + 1;
                minVal = Math.min(minVal, oldLeftVal + (word2.charAt(i2) == c1 ? 0 : 2));
                oldLeftVal = dp[i2 + 1];
                dp[i2 + 1] = minVal;
            }
        }
        return dp[dp.length - 1];
    }
}
