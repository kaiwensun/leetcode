class Solution {
    public int[][] rangeAddQueries(int n, int[][] queries) {
        int[][] res = new int[n][];
        for (int i = 0; i < n; i++) {
            res[i] = new int[n];
        }
        for (int[] q : queries) {
            q[2]++; q[3]++;
            res[q[0]][q[1]]++;
            if (q[3] < n) res[q[0]][q[3]]--;
            if (q[2] < n) {
                res[q[2]][q[1]]--;
                if (q[3] < n) res[q[2]][q[3]]++;
            }
        }
        for (int i = 0; i < n; i++) {
            int left = 0;
            for (int j = 0; j < n; j++) {
                left += res[i][j];
                res[i][j] = (i == 0 ? 0 : res[i - 1][j]) + left;
            }
        }
        return res;
    }
}

