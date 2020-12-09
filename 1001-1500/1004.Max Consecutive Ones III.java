class Solution {
    public int longestOnes(int[] A, int K) {
        int l = 0;
        int res = 0;
        for (int r = 0; r < A.length; r++) {
            if (A[r] == 0) {
                if (K > 0) {
                    K--;
                } else {
                    while (A[l] == 1) {
                        l++;
                    }
                    l++;
                }
            }
            res = Math.max(res, r - l + 1);
        }
        return res;
    }
}

