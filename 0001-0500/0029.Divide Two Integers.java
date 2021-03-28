class Solution {
    public int divide(long dividend, long divisor) {
        if (dividend == 0x80000000) {
            if (divisor == 1) return 0x80000000;
            if (divisor == -1) return 0x7FFFFFFF;
        }
        int res = 0;
        boolean neg = (dividend < 0) ^ (divisor < 0);
        dividend = Math.abs(dividend);
        divisor = Math.abs(divisor);
        while (dividend >= divisor) {
            int times = 1;
            long cur = divisor;
            while (cur << 1 <= dividend) {
                cur <<= 1;
                times <<= 1;
            }
            res += times;
            dividend -= cur;
        }
        return neg ? -res : res;
    }
}

