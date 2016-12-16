public class Solution {
    public boolean isMatch(String s, String p) {
        boolean[][] dp  = new boolean[s.length()+1][p.length()+1];
        dp[0][0] = true;
        for(int j = 0;j<p.length();j++){
            for(int i = -1;i<s.length();i++){
                if(p.charAt(j)=='*'){
                    dp[i+1][j+1] = dp[i+1][j];
                }else if(j+1<p.length() && p.charAt(j+1)=='*'){
                    dp[i+1][j+1] = (dp[i+1][j]) || (i>=0 && (dp[i][j+1] || dp[i][j]) && (p.charAt(j)=='.' || p.charAt(j)==s.charAt(i)));
                }else{
                    dp[i+1][j+1] = i>=0 && dp[i][j] && (p.charAt(j)=='.' || p.charAt(j) == s.charAt(i));
                }
            }
        }
        //printdp(dp);
        return dp[s.length()][p.length()];
    }
    private void printdp(boolean[][] dp){
        for(boolean[] row : dp){
            for(boolean b:row){
                System.out.print(b?1:0);
            }
            System.out.println();
        }
    }
}
