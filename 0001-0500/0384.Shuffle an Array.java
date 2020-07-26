class Solution {
    private final int[] nums;
    private final int[] shuffled;
    private final Random r = new Random();

    public Solution(int[] nums) {
        this.nums = nums;
        this.shuffled = new int[nums.length];
        reset();
    }
    
    /** Resets the array to its original configuration and return it. */
    public int[] reset() {
        for (int i = 0; i < nums.length; i++) {
            shuffled[i] = nums[i];
        }
        return shuffled;
    }
    
    /** Returns a random shuffling of the array. */
    public int[] shuffle() {
        if (shuffled.length == 0) {
            return shuffled;
        }
        int homeless = shuffled[shuffled.length - 1];
        for (int i = shuffled.length - 1; i >= 0; i--) {
            int target = r.nextInt(i + 1);
            int tmp = shuffled[target]; shuffled[target] = shuffled[i]; shuffled[i] = tmp;
        }
        return shuffled;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */
