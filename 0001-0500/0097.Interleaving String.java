class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        if (s1.length() + s2.length() != s3.length()) {
            return false;
        }
        boolean[] dp = new boolean[] {true};
        boolean[] filling;
        boolean possible = true;
        for (int s3Index = 0; possible && s3Index < s3.length(); s3Index++) {
            filling = new boolean[Math.min(s1.length() + 1, s3Index + 2)];
            char c3 = s3.charAt(s3Index);
            possible = false;
            for (int s1Index = Math.max(0, s3Index - s2.length()); s1Index < Math.min(s1.length(), s3Index + 1); s1Index++) {
                filling[s1Index + 1] = filling[s1Index + 1] || (dp[s1Index] && s1.charAt(s1Index) == c3);
                possible = possible || filling[s1Index + 1];
            }
            for (int s2Index = Math.max(0, s3Index - s1.length()); s2Index < Math.min(s2.length(), s3Index + 1); s2Index++) {
                int s1Index = s3Index - s2Index - 1;
                filling[s1Index + 1] = filling[s1Index + 1] || (dp[s1Index + 1] && s2.charAt(s2Index) == c3);
                possible = possible || filling[s1Index + 1];
            }
            dp = filling;
        }
        return dp[dp.length - 1];

    }
}

