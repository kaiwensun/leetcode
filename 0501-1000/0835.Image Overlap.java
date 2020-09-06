class Solution {
    public int largestOverlap(int[][] A, int[][] B) {
        int res = largestOverlap(A, B, 0);
        res = Math.max(res, largestOverlap(B, A, res));
        return res;
    }
    private int largestOverlap(int[][] A, int[][] B, int known_max) {
        int res = known_max, size = A.length;
        for (int shift_i = 0; shift_i < size; shift_i++) {
            if (size * (size - shift_i) < res) {
                break;
            }
            for (int shift_j = 0; shift_j < size; shift_j++) {
                if ((size - shift_j) * (size - shift_i) < res) {
                    break;
                }
                res = Math.max(res, overlap(A, B, shift_i, shift_j, res));
            }
        }
        return res;
    }
    private int overlap(int[][] A, int[][] B, int shift_i, int shift_j, int known_max) {
        int[] cnt = new int[] {0, 0};
        for (int i = shift_i; i < A.length; i++) {
            for (int j = shift_j; j < A[i].length; j++) {
                cnt[A[i][j] & B[i - shift_i][j - shift_j]]++;
                if (cnt[0] > A.length * A[0].length - known_max) {
                    return -1;
                }
            }
        }
        return cnt[1];
    }
}

