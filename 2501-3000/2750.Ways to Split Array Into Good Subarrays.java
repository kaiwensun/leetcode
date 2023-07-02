class Solution {
    private final int MOD = 1_000_000_007;
    public int numberOfGoodSubarraySplits(int[] nums) {
        List<Integer> indexes = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                indexes.add(i);
            }
        }
        if (indexes.size() == 0) {
            return 0;
        }
        return (int) endsWithTheOneAt(0, indexes);
    }
    private long endsWithTheOneAt(int i, List<Integer> indexes) {
        if (i == indexes.size() - 1) {
            return 1;
        }
        return (indexes.get(i + 1) - indexes.get(i)) * endsWithTheOneAt(i + 1, indexes) % MOD;
    }
}

