class Solution {
    public int[] evenOddBit(int n) {
        int[] res = new int[2];
        while (n != 0) {
            res[0] += n & 1;
            n >>= 1;
            res[1] += n & 1;
            n >>= 1;
        }
        return res;
    }
}

