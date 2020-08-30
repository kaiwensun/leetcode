class Solution {
    public int minOperations(int[] nums) {
        int mask = 0;
        int bits = 0;
        for (int num : nums) {
            mask |= num;
            bits += Integer.bitCount(num);
        }
        for (int shift : new int[] {1, 2, 4, 8, 16}) {
            mask |= mask >> shift;
        }
        return Math.max(Integer.bitCount(mask) + bits - 1, 0);
    }
}
