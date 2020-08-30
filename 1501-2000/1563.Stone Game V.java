class Solution {
    private int[] prefix;
    private int[][] table;
    
    private void initTable(int size) {
        table = new int[size][];
        for (int i = 0; i < size; i++) {
            table[i] = new int[size + 1];
            for (int j = 0; j <= size; j++) {
                table[i][j] = -1;
            }
            table[i][i + 1] = 0;
        }
    }
    private void initPrefix(int[] stoneValue) {
        prefix = new int[stoneValue.length + 1];
        for (int i = 0; i < stoneValue.length; i++) {
            prefix[i + 1] = prefix[i] + stoneValue[i];
        }
    }
    private int sumRange(int i, int j) {
        return prefix[j] - prefix[i];
    }
    private int dp(int i, int j) {
        if (table[i][j] == -1) {
            int res = 0;
            for (int split = i + 1; split < j; split++) {
                int lSum = sumRange(i, split);
                int rSum = sumRange(split, j);
                if (lSum >= rSum) {
                    res = Math.max(res, rSum + dp(split, j));
                }
                if (lSum <= rSum) {
                    res = Math.max(res, lSum + dp(i, split));
                }
            }
            table[i][j] = res;
        }
        return table[i][j];
    }
    public int stoneGameV(int[] stoneValue) {
        initPrefix(stoneValue);
        initTable(stoneValue.length);
        return dp(0, stoneValue.length);
    }
}
