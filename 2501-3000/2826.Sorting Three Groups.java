class Solution {
    public int minimumOperations(List<Integer> nums) {
        int start1 = 0;
        int res = nums.size();
        for (int start2 = 0; start2 <= nums.size(); start2 ++) {
            for (int start3 = start2; start3 <= nums.size(); start3++) {
                int cur = 0;
                int[] starts = new int[] {start1, start2, start3, nums.size()};
                for (int target = 1; target <= 3; target++) {
                    for (int i = starts[target - 1]; i < starts[target]; i++) {
                        if (nums.get(i) != target) {
                            cur++;
                        }
                    }
                }
                res = Math.min(res, cur);
            }
        }
        return res;
    }
}

