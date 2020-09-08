class Solution {
    public int deleteAndEarn(int[] nums) {
        Arrays.sort(nums);
        int take = 0;
        int avoid = 0;
        int prevEndInd = -1;
        int prev = 0;
        int curr = 0;
        if (nums.length > 0) {
            curr = nums[0];
            prev = nums[0] - 2;
        }
        for (int i = 0; i < nums.length; ++i) {
            if (i == nums.length - 1 || nums[i + 1] != curr) {
                int strike = curr * (i - prevEndInd);
                if (prev + 1 == curr) {
                    int oldAvoid = avoid;
                    avoid = Math.max(avoid, take);
                    take = oldAvoid + strike;
                } else {
                    avoid = Math.max(take, avoid);
                    take = avoid + strike;
                }
                prev = curr;
                if (i < nums.length - 1) {
                    curr = nums[i + 1];
                }
                prevEndInd = i;
            }
        }
        return Math.max(avoid, take);
    }
}
