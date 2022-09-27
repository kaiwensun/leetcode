class Solution {
    public int[] smallestSubarrays(int[] nums) {
        int res[] = new int[nums.length];
        int[] bits = new int[32];
        int j = nums.length - 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            countBits(nums[i], bits, 1);
            while (j > i && isReduntand(nums[j], bits)) {
                countBits(nums[j--], bits, -1);
            }
            res[i] = j - i + 1;
        }
        return res;
    }

    private boolean isReduntand(int num, int[] bits) {
        for (int i = 0; num != 0; i++) {
            if ((num & (1 << i)) != 0) {
                num ^= 1 << i;
                if (bits[i] == 1) {
                    return false;
                }
            }
        }
        return true;
    }

    private void countBits(int num, int[] bits, int diff) {
        for (int i = 0; num != 0; i++) {
            if ((num & (1 << i)) != 0) {
                num ^= 1 << i;
                bits[i] += diff;
            }
        }
    }
}

