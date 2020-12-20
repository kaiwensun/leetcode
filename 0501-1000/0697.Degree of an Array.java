class Solution {
    public int findShortestSubArray(int[] nums) {
        Map<Integer, Integer> start = new HashMap<>();
        Map<Integer, Integer> end = new HashMap<>();
        Map<Integer, Integer> count = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            start.putIfAbsent(nums[i], i);
            end.put(nums[i], i);
            count.put(nums[i], count.getOrDefault(nums[i], 0) + 1);
        }
        int max_count = 0;
        int res = nums.length;
        for (int num : count.keySet()) {
            if (count.get(num) > max_count) {
                max_count = count.get(num);
                res = end.get(num) - start.get(num) + 1;
            } else if (count.get(num) == max_count) {
                res = Math.min(res, end.get(num) - start.get(num) + 1);
            }
        }
        return res;
    }
}

