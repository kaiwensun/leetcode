class Solution {
    public int longestSubarray(int[] nums) {
        int max = Arrays.stream(nums).max().getAsInt();
        int cur = 0, res = 0;
        for (int num : nums) {
            if (num == max) {
                res = Math.max(res, ++cur);
            } else {
                cur = 0;
            }
        }
        return res;
    }
}

