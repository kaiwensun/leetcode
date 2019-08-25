class Solution {
    public int longestWPI(int[] hours) {
        int res = 0;
        int benefit = 0;
        List<Integer> seen = new ArrayList<>();
        for (int i = 0; i < hours.length; i++) {
            benefit += hours[i] > 8 ? 1 : -1;
            if (benefit < 0 && -benefit > seen.size()) {
                seen.add(i);
            }
            if (benefit > 0) {
                res = Math.max(res, i + 1);
            } else {
                res = Math.max(res, i - (seen.size() > -benefit ? seen.get(-benefit) : Integer.MIN_VALUE));
            }
        }
        return res;
    }
}
