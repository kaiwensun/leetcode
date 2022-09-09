class Solution {
    public int longestNiceSubarray(int[] nums) {
        int[] lastSeenOne = new int[30];
        Arrays.fill(lastSeenOne, -1);
        int res = 0;
        int prevLeftMost = -1;
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int leftMost = -1;
            for (int bitIdx = 0, mask = 1; mask <= num; mask <<= 1, bitIdx++) {
                if ((mask & num) != 0) {
                    leftMost = Math.max(leftMost, lastSeenOne[bitIdx]);
                    lastSeenOne[bitIdx] = i;
                }
            }
            prevLeftMost = Math.max(prevLeftMost, leftMost);
            res = Math.max(res, i - prevLeftMost);
        }
        return res;
    }
}

