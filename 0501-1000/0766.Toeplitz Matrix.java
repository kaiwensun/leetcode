class Solution {
    public boolean isToeplitzMatrix(int[][] matrix) {
        for (int k = 0; k < matrix.length + matrix[0].length - 1; k++) {
            int j = Math.max(0, k - matrix.length + 1);
            int i = Math.max(0, matrix.length - 1 - k);
            int num = matrix[i][j];
            while (i < matrix.length && j < matrix[0].length) {
                if (num != matrix[i++][j++]) {
                    return false;
                }
            }
        }
        return true;
    }
}

