class Solution {
    public int[][] flipAndInvertImage(int[][] A) {
        for (int[] row: A) {
            int i = 0;
            int j = row.length - 1;
            for (int t = 0; t < (A.length + 1) / 2; t++) {
                int tmp = row[i];
                row[i++] = 1 - row[j];
                row[j--] = 1 - tmp;
            }
        }
        return A;
    }
}
