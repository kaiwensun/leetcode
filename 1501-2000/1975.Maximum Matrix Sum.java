class Solution {
    public long maxMatrixSum(int[][] matrix) {
        int count_neg = 0;
        long sum = 0;
        long min_abs = Integer.MAX_VALUE;
        for (int[] row : matrix) {
            for (int num : row) {
                count_neg ^= num;
                min_abs = Math.min(min_abs, Math.abs(num));
                sum += Math.abs(num);
            }
        }
        return count_neg < 0 ? sum - min_abs * 2 : sum;
    }
}

