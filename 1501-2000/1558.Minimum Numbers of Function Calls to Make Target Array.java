class Solution {
    public int minOperations(int[] nums) {
        int cntZeros = 0;
        int res = 0;
        while (cntZeros != nums.length) {
            cntZeros = 0;
            for (int i = 0; i < nums.length; i++) {
                if (nums[i] % 2 == 1) {
                    nums[i]--;
                    res++;
                }
                if (nums[i] == 0) {
                    cntZeros++;
                }
                nums[i] >>= 1;
            }
            if (cntZeros != nums.length) {
                res += 1;
            }
        }
        return res;
    }
}
