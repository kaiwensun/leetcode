class Solution {
    public int dominantIndex(int[] nums) {
        if (nums.length == 1) {
            return 0;
        }
        int largestIndex = 0;
        int fstLargest = -1;
        int sndLargest = -1;
        for(int i = 0; i < nums.length; i++) {
            if (nums[i] > fstLargest) {
                sndLargest = fstLargest;
                fstLargest = nums[i];
                largestIndex = i;
            } else if (nums[i] > sndLargest) {
                sndLargest = nums[i];
            }
        }
        return fstLargest >= sndLargest * 2 ? largestIndex : -1;
    }
}

