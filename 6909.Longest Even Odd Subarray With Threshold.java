class Solution {
    public int longestAlternatingSubarray(int[] nums, int threshold) {
        int res = 0;
        int l = 0;
        for (int r = l + 1; r <= nums.length; r++) {
            while (l < nums.length && (nums[l] > threshold || nums[l] % 2 == 1)) {
                l++;
            }
            if (l == nums.length) break;
            r = Math.max(r, l + 1);
            if (r == nums.length || nums[r] > threshold || (l != r && nums[r - 1] % 2 == nums[r] % 2)) {
                res = Math.max(res, r - l);
                l = r;
            }
        }
        return res;
    }
}

