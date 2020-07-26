class Solution {
    public int findTargetSumWays(int[] nums, int S) {
        Map<Integer, Integer> counter = new HashMap<>();
        counter.put(0, 1);
        for (int num : nums) {
            Map<Integer, Integer> newCounter = new HashMap<>();
            counter.entrySet().forEach(entry -> {
                Arrays.asList(num, -num).forEach(diff -> {
                   int sum = entry.getKey() + diff;
                    newCounter.put(sum, newCounter.getOrDefault(sum, 0) + entry.getValue()); 
                });
            });
            counter = newCounter;
        }
        return counter.getOrDefault(S, 0);
    }
}
