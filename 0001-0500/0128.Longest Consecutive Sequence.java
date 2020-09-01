class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>(nums.length);
        for (int num : nums) {
            set.add(num);
        }
        int maxCnt = 0;
        while (!set.isEmpty()) {
            int num = set.iterator().next();
            int cur = num;
            int cnt = 0;
            while (set.remove(cur--)) {
                cnt ++;
            }
            cur = num + 1;
            while (set.remove(cur++)) {
                cnt ++;
            }
            maxCnt = Math.max(maxCnt, cnt);
        }
        return maxCnt;
    }
}
