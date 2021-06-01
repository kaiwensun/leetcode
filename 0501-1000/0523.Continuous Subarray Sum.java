class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        Set<Integer> seen = new HashSet<>();
        int sum = 0;
        int prevsum = 0;
        for (int num : nums) {
            sum = (sum + num) % k;
            if (seen.contains(sum)) {
                return true;
            }
            seen.add(prevsum);
            prevsum = sum;
        }
        return false;
    }
}

