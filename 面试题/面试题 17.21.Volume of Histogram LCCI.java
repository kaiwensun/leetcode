class Solution {
    public int trap(int[] height) {
        int l = 0, r = height.length - 1;
        int res = 0, lmax = 0, rmax = 0;
        while (l <= r) {
            if (height[l] < height[r]) {
                lmax = Math.max(height[l], lmax);
                res += lmax - height[l++];
            } else {
                rmax = Math.max(height[r], rmax);
                res += rmax - height[r--];
            }
        }
        return res;
    }
}

